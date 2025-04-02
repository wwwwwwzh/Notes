# Implicit (other than NeRF)
## Occupancy Networks
implicitly represent the 3D surface as the continuous decision boundary of a deep neural network classifier. f(xyz, latent)->[0,1]. Can be used to do 3D reconstruction from single images, noisy point clouds and coarse discrete voxel grids. Loss=cross entropy between true occupancy and prediction + KL of latent code prior

## Deep SDF
3D supervision. Directly predicts signed distance from surface given xyz. Used auto decoder to optimize jointly on a shape prior. 

## SRN
Proposed a differentiable ray marching algorithm and represented scene as coordinate->color.

![SRN](/images/SRN.png)
1. shoot rays from image coordinates to world, initial distance 0.05
2. 3d world coord to MLP and get features
3. features go to LSTM to compute step length (sphere tracing)
4. march ray with step length from 3 and iterate for a fixed amount of times
5. final coordinate's feature pass 1x1 conv to get color

We can see that NeRF wins by using a naturally differentiable algorithm that's well established in traditional graphics.

# NeRF
https://dellaert.github.io/NeRF22/

## Improvements
### [NeuS NeurIPS 21 SL](https://lingjie0206.github.io/papers/NeuS/)
NeRF's surface reconstruction is noisy due to its density field nature. Use SDF instead. To optimize SDF without 3d gt, convert signed distance to density and do volume rendering. One key challenge is to construct an unbiased and occlusion aware weight function

![](/images/neus.png)
f is sdf, sigma and ɸ below is logistic density function with learnable variance based on sdf. 
![](/images/neus2.png)

### [Mip NeRF ICCV 21 Oral](https://jonbarron.info/mipnerf/)
Color of a pixel is determined by the whole frustum instead of a ray. NeRF's ray sampling thus causes aliasing problems. Solution: sample sub-volume from the conical frustum and approximate with multivariate gaussian and use expected value. A new positional encoding is also designed for this.

### [Mip360 CVPR 22 Oral](https://jonbarron.info/mipnerf360/)
"We use non-linear scene parameterization, online distillation, and a novel distortion-based regularizer to overcome the challenges presented by unbounded scenes"

### [NeRF Studio](https://docs.nerf.studio/en/latest/)
The library supports a more interpretable implementation of NeRFs by modularizing each component. With more modular NeRFs, we hope to create a more user-friendly experience in exploring the technology.

### [Zip NeRF](https://jonbarron.info/zipnerf/)


## Dynamic
### Time + NeRF
Can give reasonable results in low motion parts of the scene (with enough features). Though theoretically each time input can interrupt the whole scene representation thus give bad reconstruction near camera for all frames, in practice time and xyz are input to the first layer (skipped to 4th too) and they become entangled in the MLP layers.

[Plain Time+NeRF with predicted depth](https://video-nerf.github.io/)


### NSFF
Monocular dynamic reconstruction means one view point per frame. How to get more multi-view constraint? Use MLP to model both radiance and scene flow. For each time, we then have points mapped from previous and next time. Because those points are shot from different poses, they can constraint current time view if flow is correct. To get more priors, also use depth prediction and optical flow prediction. These priors gradually diminish during training. 

### Dynamic NeRF
Well written code. Only difference from NSFF is blending from dynamic nerf and some different engineering choice during training. 

It's difficult to train since all blending, forward and backward flow, and rgbd are produced by the same features from the last layer of MLP which makes this feature space highly entangled. 

------------------------------------------------
# Explicit
# Point
### [PointNet CVPR 17](http://stanford.edu/~rqi/pointnet/docs/cvpr17_pointnet_slides.pdf)
<img width="1000" alt="Screen Shot 2023-01-04 at 2 24 20 PM" src="https://user-images.githubusercontent.com/36484215/210652646-6a69efd5-b508-4a75-8166-88257994d5dd.png">
Note mlp(64,64) means two mlp with output feature size 64 and 64.

1. Global max pooling and point wise MLP to enforce permutation invariance (points with different ordering should be the same scene)
2. Learned transformation to enforce invariance under geometric transformations (rotation)

All MLPs are shared between points which means every feature up to max pool is local (point specific). A 1024 vector represents information from all features of all points with max pool. All N final outputs are concerned with the 1024 global feature and their own 64 local features.

> Note1: transformation on coordinate points and on feature space with a predicted transformation matrix combined yields a 2% boost on ModelNet40 classification

> Note2: Attention and average pooling yields worse performance as the symmetric function compared to max pool

> Note3: the max pooling can be seen as key point selection where some points' some features are selected as globally important information

> Note4: input for segmentation, in addition to x,y,z normalized location (0-1) and RGB (9 in total)

### [PointNet++](https://arxiv.org/pdf/1706.02413.pdf)
![](/images/pointnet%2B%2B.png)
PointNet does not capture local structures. Solution: sample->grouping->pointnet block repeated

- FPS as sampling. 
- Ball query for grouping (more generalizable across space with varying density compared to kNN) [N (d+C)]->[N' K (d+C)] note that K varies across groups N'
- coordinate->local coord. [N' K (d+C)] -> [N' (d+C')]
- combine features from different scales:
    - concat local features from different scales (simultaneously not propagate from raw to lower scale)
    - concat 2 scales, one below current layer one from current layer

> Note1: random input drop with p=0.95 is used to train

### [FrustumNet](https://arxiv.org/pdf/1711.08488.pdf)
![](/images/frustumnet.png)
![](/images/frustumnet2.png)
![](/images/frustumnet-arc.png)

3D bounding box and classification. Use 2D detection pipeline and reproject box to 3d frustum. Estimate with points inside the frustum (4d x,y,z and intensity).

> Note1: multiple transformations to canonical space is crucial (frustum, masked points, centered space)

> Note2: pointnet++ provides a minor performance boost.

> Note3: birds eye view has better performance

### [VoxelNet](https://arxiv.org/pdf/1711.06396.pdf)

### [Point Pillar]()
![](/images/ppillar.png)

3D bounding box and classification. Convert 3d point cloud to 2d feature plane by partitioning the point cloud from bird's eye view to vertical pillars. Each pillar generate a feature vector with a simple PixelNet(one linear on each point, BN, relu and max pool). This way the point cloud becomes a traditional 2d image. The point encoder (PointNet) on pillars and global 2D CNN learn jointly to aggregate useful information and generate bounding boxes. 

### [Point Transformer]()
> The transformer family of models is particularly appropriate for point cloud processing because the self-attention operator is in essence a set operator: it is invariant to permutation and cardinality of the input elements.

Vector attention: attention weights are vectors that can modulate individual feature channels (K^TQ in scalar attention)

- Points->features
- Attention with nearby points' features: features->K, Q, V(linear), relative position->δ(mlp); Q-K+δ->attention weights(mlp); attention weights*(V+δ)->output


# Voxel
## NeRF Inspired
### Plenoxel
> the key element of Neural Radiance Fields is not the neural network but the differentiable volumetric renderer.

> opacity in the Neural Volumes formula is absolute and ray-independent whereas opacity in the Max formula denotes the fraction of incoming light that each sample absorbs, a ray-dependent quantity. As we show, the Max formula results in substantially better performance; we suspect this difference is due to its more physically-accurate modeling of transmittance.

Trilinear interpolation of spherical harmonics at 256/512^3 resolution. Grid is all entries where empty is null.

### NSVF
octree + MLP

### Direct Voxel
feature + density grid, coarse to dense, color from feature grid+shallow MLP, density from post activation

low density init
#### Instant NGP
replace dense grid with 16 hash tables of size 2^14-24. Each table represents a different resolution. Results are concated and passed to shallow MLP. 

------------------------------------------------
# Few Shot NVS
## NeRF Backbone
### [PixelNerf 2021](https://alexyu.net/pixelnerf/)
Nerf conditioned on feature volume.
![](/images/pixelnerf.png)

Nerf but other than normal 5d input, condition each point also on image features provided by the conditioned image (project nerf input point to image space on input image). This way the model learns to decode image features in 3d supervised by volume rendering constraint. Not very good result but seminal work.

> It's unclear why x is necessary as mlp input; possible explanation is they model the problem as conditional nerf i.e. radiance field conditioned on feature volume f(x,d; W(x))->(c, σ) so f is still a nerf. A better approach would be C(x,d): f(W(x),d)->(c, σ) which is used in most future work but this formulation is more similar to light field

## Light Field
### [Light Field Networks 2021 SL](https://www.vincentsitzmann.com/lfns/)
Light field conditioned on scene prior encoded from input image. 
![](/images/lfn.png)

Scene prior is necessary because 4d light field itself isn't 3d consistent (nerf addresses this problem by passing view direction late but light field can't separate its 4d inputs). 

> About light field: "Adelson et al. introduced the 5D plenoptic function as a unified representation of information in the early visual system. Levoy et al. and, concurrently, Gortler et al. introduced light fields in computer graphics as a 4D sampled scene representation for fast image-based rendering. Light fields have since enjoyed popularity as a representation for novel view synthesis and computational photography"

> More: "while the light field only encodes appearance explicitly, its derivatives encode geometry information about the underlying 3D scene"

> current formulation of LFNs does not outperform pixelNeRF. We note, however, that local conditioning methods solve a different problem. Rather than learning a prior over classes of objects, local conditioning methods learn priors over patches, answering the question “How does this image patch look like from a different perspective?”. As a result, this approach does not learn a latent space of neural scene representations. (Note that pixelNeRF does learn a latent space of feature volumes of neural scene representations. this paragraph is ambiguous in this sense but should be understood in a local patch encoding i.e. pixel aligned feature space perspective)

## Local Patch Based
### [IBRNet 2021](https://ibrnet.github.io/)
![](/images/ibr.png)
![](/images/ibr2.png)

### [NeRFormer/CO3D ICCV 21](https://arxiv.org/pdf/2109.00512)
- 50 categories 19k objects
Similar to IBR net
![](/images/nerformer.png)

### [NeRFusion CVPR 22 Oral](https://jetd1.github.io/NeRFusion-Web/)
![](/images/nerfusion.png)

### [Light Field Neural Rendering 2022 Oral](https://light-field-neural-rendering.github.io/)
Light field formulation with epipolar feature aggregation and learned rendering function (both transformers). 
![](/images/nlf.png)


### [Generalizable Patch-Based Neural Rendering 2022 Oral](https://mohammedsuhail.net/gen_patch_neural_rendering/)
More complex than IBRNet (more transformers) but similar idea. Slightly better result than IBRNet
![](/images/gpnr.gif)

> ray representations (6d Plucker coordinates) are used as positional encoding in the transformers.

> 10 reference views and 20 depth points for training and evaluation

## Geometry + Diffusion
### [GENVS 2023](https://nvlabs.github.io/genvs/)
image (>=1) to image through 3d feature volume, volume rendered latent feature image (2d) and conditional diffusion.
![](/images/genvs.png)
![](/images/genvs2.png)
![](/images/genvs3.png)

T encodes reference image as feature volume (depth=64, channel=16) and should intuitively understand how 2d image should be lifted to 3d (depth aware). Feature volume is volume rendered to feature image which makes all feature images from the same feature volume 3d consistent. Feature image gives necessary information to render a realistic image through U-net. U is trained with diffusion objective since diffusion models are good at constructing good image. 

Two problems to solve:
1. Ambiguity in extrapolation: often some parts of target view are occluded in reference image and "painting" these regions is ambiguous. Given other known parts in image, occluded regions generally follow multimodal distribution but regression (mse) training objective modals this as normal. These modals actually learn the average of all possible in-paintings of occluded regions and will produce blurry or over smooth result (pixelNeRF). Thus generative models are used to resolve this ambiguity by learning the full multimodal distribution. Note that they tried one step diffusion which is theoretically identical to MSE and it gives blurry result but high PSNR.
2. 3d consistency: existing generative methods have no 3d prior and struggle with generating geometrically consistent sequences. In their experiment, diffusion alone gives worst result. Their work builds 3d prior based on pixel aligned feature, latent 3D feature field and neural feature rendering. 
 > "The intuition is that generative novel view synthesis is identical to any other conditional image generation task—all we need to do is condition a 2D image diffusion model on the input image and the relative camera pose. However, while there are many ways of applying this conditioning, some may be more effective than others. By incorporating geometry priors in the form of a 3D feature field and neural rendering, we give our architecture a strong inductive bias towards geometrical consistency." 

Network detail:
- T: image segmentation architecture DeepLabV3+ based on ResNet50
- f: two-layer ReLU MLP with 64 channels
- U: EDM based on DDPM++

Implementation details:
- Multiview aggregation: max pool and weighted average pool have similar result as average pool (used in paper)
- Auto-regressive conditioning schemes (frame-to-frame flicker & drift/loop closure tradeoff): 1) condition on the input image(s), the most recently generated rendering, and five previously generated images, selected at random. (baseline) 2) two pass, condition on only the nearest 4 frames during the second pass
- Stochastic Conditioning (3DiM comparison): autoregressive to a single image randomly sampled from all previously generated images. autoregressive synthesis method performs slightly better
- Training: randomly select 1-3 input image and produce 1 randomly selected target image 
- c. 100 A100 GPU hours for training

Comparison with other work:
- Pixelnerf:
- 


## Diffusion Based




------------------------------------------------
# Generative
## NeRF Backbone
### [Generative NeRF](https://arxiv.org/abs/2007.02442)
Model p(x), where x is distribution of real 3d objects, with Gθ. Given shape and appearance prior, output a nerf representation of the 3d object. GAN training. 
![](/images/graf.png)
![](/images/graf1.png)

### [giraffe CVPR 21 BP](https://m-niemeyer.github.io/project-pages/giraffe/index.html)
Similar to GRAF but disentangle objects in a scene with multiple shared GRAF.

![](/images/giraffe.png)

A real world scene may have: multiple objects, and multiple viewing angle and transformation on each object.

### [CLIP NeRF 21](https://arxiv.org/abs/2112.05139)
Feed forward generation. Given caption output a nerf representation of the described object. First train like GRAF with GAN loss, then fix conditional nerf model and train caption prior mapper with CLIP loss.

![](/images/clip-nerf.png)

> Note1: Used a deformation network to map points (position encodings) given shape encoding to displacement vector.

> Note2: "pre-trained CLIP model has the ability to support view-consistency representations for 3D-aware applications"


### [Dream Field CVPR 22 Best Poster](https://ajayj.com/dreamfields)
Per caption optimization on nerf. 
![](/images/dreamfield.png)

Trained with CLIP score so color and geometry prior lies in vision transformer that gives similar encoding for similar objects. Conditional generative prior is from CLIP that knows how to move image closer to given caption.

### [Dream Fusion ICRL 23 Spotlight](https://dreamfusion3d.github.io/)
Per caption optimization on nerf with rendered image score distillation loss.
![](/images/dream-fusion.png)

### [3D Neural Field Generation using Triplane Diffusion 23](https://jryanshue.com/nfd/)
> Shue was a highschool senior

Unconditoinal neural field (Occupancy field) generation with triplane and light MLP decoder.
![](/images/triDiff.png)
![](/images/triDiff2.png)

Convert shapenet objects to occupancy fields. Jointly learn their triplane representation and MLP for many objects (so MLP decoder is shared). Train DDPM to denoise NxNx3C image. 

Regularizations: 
- total variation on triplanes to avoid spurious high frequency information
- outlier loss on normalized occupancy value since DDPM work on (-1,1)
- explicit density regularization to learn empty space triplane feature better since sampling is mostly on object surface. This reduces artifacts.

### [Magic3D CVPR 23 HL](https://research.nvidia.com/labs/dir/magic3d/)
First dreamfusion like low res nerf optimization with instant-ngp to get coarse 3d mesh. High res latent diffusion SDS loss on rendered mesh image to update mesh directly. 
![](/images/magic3d.png)

### Others
#### [Roses](https://jiajunwu.com/papers/rose_cvpr.pdf)
Generative modeling from a single image that contains multiple instances of the same object.

## Geometry Free
### [3DiM 22](https://3d-diffusion.github.io/)

------------------------------------------------
# Misc.
### [Queries on General Neural Implicit Surfaces 22 SIGGRAPH Best Paper](https://nmwsharp.com/research/interval-implicits/)
Difficult to convert Neural Implicit Surfaces to downstream representations (mesh, points...)

------------------------------------------------
# Face
### [Dynamic Nerf for Monocular 4D Facial Avatar Reconstruction](https://arxiv.org/pdf/2012.03065.pdf)
-image->face expression latents->3d avatar
-training involves 

------------------------------------------------
# Depth Prediction
### [MVSNet](https://arxiv.org/pdf/1804.02505.pdf)
- 2D CNN to generate 32-channel feature maps downsized by four in each dimension compared with input images (HxWx3->H/4xW/4x32)
- feature map projected (repeated) to 3d cost volume
- 3d U-net to determine occupanncy
- refine depth with initial reference image


