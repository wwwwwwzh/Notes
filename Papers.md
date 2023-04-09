# Face
- [Unity The making of Enemies](https://www.youtube.com/watch?v=a0vAWyZXMWg&list=PLX2vGYjWbI0Q4rTRGHz9K71F4HnDUvGiF&index=2)
- [Ziva Face Trainer](https://zivadynamics.com/ziva-face-trainer)
- [Blender Facebuilder](https://medium.com/keentools/facebuilder-for-blender-guide-cbb10c717f7c)
- [Snap Face Mesh](https://docs.snap.com/lens-studio/references/templates/face/face-mesh#guide)

# Neural Network
## Synaptic

## Pruning
### LOTTERY TICKET HYPOTHESIS
Train a network, prune low magnitude weights, revert the rest to initialization state, train again, iterate several times.

When randomly reinitialized, winning tickets perform far worse, meaning structure alone cannot explain a winning ticket’s success.

One possible explanation for this behavior is the good initial weights are close to their final values after training—that in the most extreme case, they are already trained. However, experiments show the opposite—that the winning ticket weights move further than other weights.

we hypothesize that the structure of our winning tickets encodes an inductive bias customized to the learning task at hand. Cohen & Shashua (2016) show that the inductive bias embedded in the structure of a deep network determines the kinds of data that it can separate more parameter-efficiently than can a shallow network

#### Early Bird Tickets
we discover for the first time that the winning tickets can be identified at a very early training stage, which we term as Early-Bird (EB) tickets, via low- cost training schemes

--------------------------------------------
# 2D Vision
## CNN
### Inside NN (https://youtu.be/gCJCgQW_LKc)
[Visualizing and Understanding Convolutional Networks](https://arxiv.org/pdf/1311.2901.pdf): 1) forward all images in dataset, find most activated activations, deconv to reconstruct, also find the original part of image. 2) saliency map (gradient of category score on each pixel) 3) occlusion sensitivity

<img width="600" alt="Screen Shot 2023-01-03 at 7 40 22 PM" src="https://user-images.githubusercontent.com/36484215/210474522-3916ad21-88f6-4372-95f9-41ea43c99db1.png">

> saliency map is not as good in object localization as specialized algorithms

### [Object Detection](https://www.coursera.org/learn/convolutional-neural-networks)
#### RCNN
- use selective search to extract 2000 regions from the image as region proposals.
- run CNN on each of the 2000 regions

#### [Yolo](https://arxiv.org/pdf/1506.02640.pdf)
<img width="400" alt="Screen Shot 2023-01-14 at 3 50 54 PM" src="https://user-images.githubusercontent.com/36484215/212498622-bb463112-e95f-4ac8-979b-f5476ba1376d.png">

<img width="400" alt="Screen Shot 2023-01-14 at 3 50 12 PM" src="https://user-images.githubusercontent.com/36484215/212498594-d42d85ee-d5f5-4d5c-b09d-3d55e66332bd.png">

## Autoencoder
https://lilianweng.github.io/posts/2018-08-12-vae/

Autocoder is invented to reconstruct high-dimensional data using a neural network model with a narrow bottleneck layer in the middle.

The encoder network essentially accomplishes the dimensionality reduction, just like how we would use Principal Component Analysis (PCA) or Matrix Factorization (MF) for

If encoder and decoder both have only one linear layer, this will result in a projection problem where projection hyperplane with minimal euclidean error is found. If we have a complex enough encoder decoder, it can essentially map every input to 1,2,3... and be able to reconstruct them.

### Variational Autoencoder
#### [Intuition](https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73)
Plain autoencoders lack interpretable and exploitable structures in the latent space (lack of regularity) thus can't sample good images. This is because autoencoder is solely trained to encode and decode with as few loss as possible, no matter how the latent space is organized.

We want continuity (two close points in the latent space should not give two completely different contents once decoded) and completeness (for a chosen distribution, a point sampled from the latent space should give “meaningful” content once decoded).

Plain autoencoders overfit by either having low variance or making mean far from each other, thus we encourage the distribution to be normal.

![](/images/vae-reg.png)

#### Formal
VAE maps input into a distribution instead of a fixed vector. 

1. want argmaxΣlogpθ(x) where x is real data
2. pθ(x)=∫p(x|z)p(z)dz which is intractable
3. instead of computing p(x|z)p(z) for every z, estimate p(z|x) and compute p(x) by sampling from estimated z distribution, 

For computing loss:
1. want KL(q(z|x)|p(z|x))
2. 

### VQ-VAE
learns a discrete latent variable by the encoder

## [GANs](https://lilianweng.github.io/posts/2017-08-20-gan/)
### [Progressive GANs](https://arxiv.org/pdf/1710.10196.pdf)
![](/images/progGAN.png)
### StyleGAN
![](/images/styleGAN.png)
![](/images/styleGAN2.png)

### Image Translation
#### [Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/abs/1611.07004)
Apply Conditional GANs on many image to image generation problems.

#### [Multimodal Unsupervised Image-to-Image Translation](https://arxiv.org/abs/1804.04732)
Problem: image mapping (sketch to image, colorization, style transfer...) or translating image to another domain (p(x'|x)) is multimodal but existing approaches assume a deterministic or unimodal mapping.

Solution: uniform content space but different style space to approximate this multimodal distribution.

![](/images/multimodal-itoi.png)
![](/images/multimodal-itoi2.png)

## Diffusion
- https://jalammar.github.io/illustrated-stable-diffusion/
- https://huggingface.co/blog/annotated-diffusion
- https://yang-song.net/blog/2021/score/

A (denoising) diffusion model is like other generative models such as Normalizing Flows, GANs or VAEs: they all convert noise from some simple distribution to a data sample. Diffusion model learns to gradually denoise data starting from pure noise.

In traditional generative models like VAE or autoregressive models, we model probability density function over input data to approximate true data distribution (probability of every image). This results in intractable normalizing constant. So we instead learn a *score function* defined as gradient of log of probability density function. We can learn this by score matching.

Once we have the score function, we use Langevin dynamics which provides an MCMC procedure to sample from distribution p(x)

![](/images/score-multi-density.png)
First problem for naive implementation is inaccurate score for low density region since we don't have many samples to learn from. Our solution is to perturb data points with noise and train score-based models on the noisy data points instead.

In addition, we use multiple scales of noise perturbations simultaneously. we estimate the score function of each noise-perturbed distribution. Then we can train a Noise Conditional Score-Based Model.

The model:
- Overview: the network takes a batch of noisy images of shape (batch_size, num_channels, height, width) and a batch of noise levels of shape (batch_size, 1) as input, and returns a tensor of shape (batch_size, num_channels, height, width)
1. a convolutional layer is applied on the batch of noisy images, and position embeddings are computed for the noise levels
2. a sequence of downsampling stages are applied. Each downsampling stage consists of 2 ResNet blocks + groupnorm + attention + residual connection + a downsample operation
3. at the middle of the network, again ResNet blocks are applied, interleaved with attention
4. next, a sequence of upsampling stages are applied. Each upsampling stage consists of 2 ResNet blocks + groupnorm + attention + residual connection + an upsample operation
5. finally, a ResNet block followed by a convolutional layer is applied.

### Conditional Diffusion
In the conditional generation setting, the data x0 has an associated conditioning signal c. The only modification that needs to be made is to inject c as a extra input to the neural network function approximators: instead of µθ(xt, t) we now have µθ(xt, t, c), and likewise for Σθ. The particular architectural choices for injecting these extra inputs depends on the type of the conditioning c

#### [Stable Diffusion](https://arxiv.org/abs/2112.10752)
![](/images/stable-diffusion.png)

- Diffusion on latent space (auto-encoder)
- OpenClip encoding of text added to all attention layers at every time step. 
## Image Transformer
### [Image GPT](https://openai.com/blog/image-gpt/)
Directly use gpt on pixels. Tested both autoregressive and bert like training.

![](/images/igpt.png)

### [Vision Transformer](https://arxiv.org/pdf/2010.11929.pdf) 
Vision Transformer has much less image-specific inductive bias than CNNs. In CNNs, locality, two-dimensional neighborhood structure, and translation equivariance are baked into each layer throughout the whole model. In ViT, only MLP layers are local and translationally equivariant, while the self-attention layers are global

![](/images/ViT.png)

### [BEiT: BERT Pre-Training of Image Transformers](https://arxiv.org/pdf/2106.08254.pdf)
BEiT models are regular Vision Transformers, but pre-trained in a self-supervised way rather than supervised. Note iGPT doesn't employ vision specific processing like using image batch or targeting discrete visual tokens

The BEIT pre-training can be viewed as variational autoencoder training

![](/images/BeIT.png)

### [DALL·E](https://openai.com/blog/dall-e/)
DALL·E is a simple decoder-only transformer that receives both the text and the image as a single stream of 1280 tokens—256 for the text and 1024 for the image—and models all of them autoregressively.
1. train a discrete VAE (256^2->32^2)
2. concatenate up to 256 BPE-encoded text
tokens with the 32 × 32 = 1024 image tokens, and
train an autoregressive transformer to model the joint
distribution over the text and image tokens.

### [DALL·E 2](https://arxiv.org/pdf/2204.06125.pdf)
Train a prior that generates a CLIP image embedding given a text caption, and a decoder that generates an image
conditioned on the image embedding (diffusion)


--------------------------------------------
# NLP
## RNN
### Inside RNN
#### [VISUALIZING AND UNDERSTANDING RECURRENT NETWORKS](https://arxiv.org/pdf/1506.02078.pdf)
"For instance, one cell is clearly acting as a line length counter, starting with a high value and then slowly decaying with each character until the next newline. Other cells turn on inside quotes, the parenthesis after if statements, inside strings or comments, or with increasing strength as the indentation of a block of code increases."

### LSTM
<img width="400" alt="Screen Shot 2023-01-15 at 2 04 57 PM" src="https://user-images.githubusercontent.com/36484215/212564313-a5ba56f3-a8be-487a-8759-8ee30f5c5992.png">

- memory is like the real memory. previous output and current input update memory. after update, memory, previous output and current input all together produce new output. new output is recursed back to the program for further thinking.
- theoretically, lstm is just like a brain.
- note that both hidden state/output and memory are vectors. forget gate has same dimension as memory and operates elementwise on memory (each scalar in memory vector controlled seperately). new memory (candidate x input gate) also has same dimension as memory and control change into memory elementwise.

## Word Embedding
### Word2Vec & GloVe

### ELMo: Context Matters
- A word has multiple meanings depending on context
- Instead of using a fixed embedding for each word, ELMo looks at the entire sentence before assigning each word in it an embedding. 
- It uses a bi-directional LSTM trained on language modeling task

## Attention 
### Transformer
[illustrated transformer](https://jalammar.github.io/illustrated-transformer/)

[counting transformer parameter](https://stackoverflow.com/questions/64485777/how-is-the-number-of-parameters-be-calculated-in-bert-model)
![](/images/transformer-encoder.png)
![](/images/transformer-dimensions.jpg)
![](/images/transformer-decoder-attention-mask.png)
Note that in inference, we keep key and value of previously generated tokens and only do calculation on the new tokens' row since all other rows won't change with this new token. so the decoder is essentially one word in one word out.

#### **Relationship with MLP**
When we go from the input Lxd to concated multihead attention output Lxd, we can just replace the attention mechanism with a mlp whose every layer has input size L\*d and has L\*d neurons. We first need 3 parallel such layers to compute q,k,v. here each row in the output should only concern each row in the input (tokens lead to their own questions and answers). So like in CNN, replacing local convolution with MLP means big MLP with lots of wasted neurons. Then we concatnate output of Q and K and pass that to a 2\*L\*d input, L\*d neurons layer to get self attention. This is a special layer in that it only contains 0 and 1s. (representing matrix multiplication as a fixed matrix multiplication of concated inputs and a "rule matrix") Next, we soft select V which is another matrix multiplication. 

In conclusion, transformer can be represented by an extremely big MLP, just like CNN. But we use a powerful inductive bias to fix most of operations.

#### **Relationship with CNN**
The receptive field of each word in transformer is the whole input sequence. This might seem weaker than CNN's local focus, but the whole input sequence is selectively attended. So in effect, it sees everything but focus on a potentially small area of interest, which makes it more powerful than local focus.

This also means that each output of attention in transformer can be seen as a feature representation like those in layered CNN.

#### **Relationship with Neuron (Hypothesis)**
If we replace transformer with an equivalent MLP and omit all 0s, we can get a sparse MLP which resembles a not too large neural network.

#### NLP's ImageNet moment has arrived
> In NLP, models are typically a lot shallower than their CV counterparts. Analysis of features has thus mostly focused on the first embedding layer, and little work has investigated the properties of higher layers for transfer learning. Transformer is paradiam shifting: going from just initializing the first layer of our models to pretraining the entire model with hierarchical representations. If learning word vectors is like only learning edges, these approaches are like learning the full hierarchy of features, from edges to shapes to high-level semantic concepts. 
> Transformer employed pretrained language models to achieve state-of-the-art on a diverse range of tasks in Natural Language (https://www.ruder.io/nlp-imagenet/)

#### Totally Understood Language?

### BERT
- Encoder only.
- Trained on dataset of 3.3 Billion words. 64 TPUs for 4 days
- Trained with Masked Language Model (50%) and Next Sentence Prediction (50%)
- Mask token is not 0, it's like any other learned token embedding
http://jalammar.github.io/illustrated-bert/
> marking the beginning of a new era in NLP

![](/images/bert-tasks.png)
![](/images/bert-feature-extraction.png)

### GPT (1,2,3)
- Decoder only
- Removed the encoder decoder cross attention block. Only major difference is mask (forward mask vs learned [MASK] token embedding).
- Trained autoregressively. In translation task, input both languages and mask target language. In summurization, input both article and summary and mask summary. In these senarios, decoder only is almost equivalent to original encoder decoder.
- 117M->1.5B->175B parameters

![](/images/decoder-only-transformer-translation.png)

### Understanding Transformer Related
#### Transformer Feed-Forward Layers Are Key-Value Memories & [Persistent Memory + Attention](https://arxiv.org/pdf/1907.01470.pdf)
- FFNN takes up 2 third of parameters.
- embedding_dim x 4*embedding_dim matrix
- each column is a key
- the second 4*embedding_dim x vocab_size matrix holds values
- each row is a distribution over all words
- If we replace FFNN with a persistent "memory matrix", where key and value from which is cross attentioned with query from attention block, we get similar results.




--------------------------------------------
# Multimodal
## Image Captioning 
### Encoder-Decoder
#### Karpathy


### Transformer
#### CLIP
![](/images/clip.png)
Both encoders are pretrained transformers. Text encoder is GPT like while image encoder is based on a vision transformer. Training involves cross-modal similarity loss and weight updates jointly on the two encoders


#### [Multimodal Neurons](https://openai.com/blog/multimodal-neurons/)
Methods to investigate function of neuron: *feature visualization*, which maximizes the neuron’s firing by doing gradient-based optimization on the input, and *dataset examples*, which looks at the distribution of maximal activating images for a neuron from a dataset.

## Misc
### 2D
#### [Semantically-Aware Object Sketching](https://clipasso.github.io/clipasso/)
--------------------------------------------
# 3D Vision
## Implicit (other than NeRF)
### Occupancy Networks
implicitly represent the 3D surface as the continuous decision boundary of a deep neural network classifier. f(xyz, latent)->[0,1]. Can be used to do 3D reconstruction from single images, noisy point clouds and coarse discrete voxel grids. Loss=cross entropy between true occupancy and prediction + KL of latent code prior

### Deep SDF

### SRN
Proposed a differentiable ray marching algorithm and represented scene as coordinate->color.

![SRN](/images/SRN.png)
1. shoot rays from image coordinates to world, initial distance 0.05
2. 3d world coord to MLP and get features
3. features go to LSTM to compute step length (sphere tracing)
4. march ray with step length from 3 and iterate for a fixed amount of times
5. final coordinate's feature pass 1x1 conv to get color

We can see that NeRF wins by using a naturally differentiable algorithm that's well established in traditional graphics.

## NeRF
### Dynamic
#### Time + NeRF
Can give reasonable results in low motion parts of the scene (with enough features). Though theoretically each time input can interrupt the whole scene representation thus give bad reconstruction near camera for all frames, in practice time and xyz are input to the first layer (skipped to 4th too) and they become entangled in the MLP layers.

[Plain Time+NeRF with predicted depth](https://video-nerf.github.io/)


#### NSFF
Monocular dynamic reconstruction means one view point per frame. How to get more multi-view constraint? Use MLP to model both radiance and scene flow. For each time, we then have points mapped from previous and next time. Because those points are shot from different poses, they can constraint current time view if flow is correct. To get more priors, also use depth prediction and optical flow prediction. These priors gradually diminish during training. 

#### Dynamic NeRF
Well written code. Only difference from NSFF is blending from dynamic nerf and some different engineering choice during training. 

It's difficult to train since all blending, forward and backward flow, and rgbd are produced by the same features from the last layer of MLP which makes this feature space highly entangled. 

## Projection
### [Multiview CNN for Classification](https://arxiv.org/pdf/1505.00880.pdf)

## Explicit
### Point
#### [PointNet](http://stanford.edu/~rqi/pointnet/docs/cvpr17_pointnet_slides.pdf)
<img width="1000" alt="Screen Shot 2023-01-04 at 2 24 20 PM" src="https://user-images.githubusercontent.com/36484215/210652646-6a69efd5-b508-4a75-8166-88257994d5dd.png">
Note mlp(64,64) means two mlp with output feature size 64 and 64.

1. Global max pooling and point wise MLP to enforce permutation invariance (points with different ordering should be the same scene)
2. Learned transformation to enforce invariance under geometric transformations (rotation)

All MLPs are shared between points which means every feature up to max pool is local (point specific). A 1024 vector represents information from all features of all points with max pool. All N final outputs are concerned with the 1024 global feature and their own 64 local features.

> Note1: transformation on coordinate points and on feature space with a predicted transformation matrix combined yields a 2% boost on ModelNet40 classification

> Note2: Attention and average pooling yields worse performance as the symmetric function compared to max pool

> Note3: the max pooling can be seen as key point selection where some points' some features are selected as globally important information

> Note4: input for segmentation, in addition to x,y,z normalized location (0-1) and RGB (9 in total)

#### [PointNet++](https://arxiv.org/pdf/1706.02413.pdf)
![](/images/pointnet%2B%2B.png)
PointNet does not capture local structures. Solution: sample->grouping->pointnet block repeated

- FPS as sampling. 
- Ball query for grouping (more generalizable across space with varying density compared to kNN) [N (d+C)]->[N' K (d+C)] note that K varies across groups N'
- coordinate->local coord. [N' K (d+C)] -> [N' (d+C')]
- combine features from different scales:
    - concat local features from different scales (simultaneously not propagate from raw to lower scale)
    - concat 2 scales, one below current layer one from current layer

> Note1: random input drop with p=0.95 is used to train

#### [FrustumNet](https://arxiv.org/pdf/1711.08488.pdf)
![](/images/frustumnet.png)
![](/images/frustumnet2.png)
![](/images/frustumnet-arc.png)

3D bounding box and classification. Use 2D detection pipeline and reproject box to 3d frustum. Estimate with points inside the frustum (4d x,y,z and intensity).

> Note1: multiple transformations to canonical space is crucial (frustum, masked points, centered space)

> Note2: pointnet++ provides a minor performance boost.

> Note3: birds eye view has better performance

#### [VoxelNet](https://arxiv.org/pdf/1711.06396.pdf)

#### [Point Pillar]()
![](/images/ppillar.png)

3D bounding box and classification. Convert 3d point cloud to 2d feature plane by partitioning the point cloud from bird's eye view to vertical pillars. Each pillar generate a feature vector with a simple PixelNet(one linear on each point, BN, relu and max pool). This way the point cloud becomes a traditional 2d image. The point encoder (PointNet) on pillars and global 2D CNN learn jointly to aggregate useful information and generate bounding boxes. 

#### [Point Transformer]()
> The transformer family of models is particularly appropriate for point cloud processing because the self-attention operator is in essence a set operator: it is invariant to permutation and cardinality of the input elements.

Vector attention: attention weights are vectors that can modulate individual feature channels (K^TQ in scalar attention)

- Points->features
- Attention with nearby points' features: features->K, Q, V(linear), relative position->δ(mlp); Q-K+δ->attention weights(mlp); attention weights*(V+δ)->output


### Voxel
#### Plenoxel
> the key element of Neural Radiance Fields is not the neural network but the differentiable volumetric renderer.

> opacity in the Neural Volumes formula is absolute and ray-independent whereas opacity in the Max formula denotes the fraction of incoming light that each sample absorbs, a ray-dependent quantity. As we show, the Max formula results in substantially better performance; we suspect this difference is due to its more physically-accurate modeling of transmittance.

Trilinear interpolation of spherical harmonics at 256/512^3 resolution. Grid is all entries where empty is null.

#### NSVF
octree + MLP

#### Direct Voxel
feature + density grid, coarse to dense, color from feature grid+shallow MLP, density from post activation

low density init
#### Instant NGP
replace dense grid with 16 hash tables of size 2^14-24. Each table represents a different resolution. Results are concated and passed to shallow MLP. 

## Few Shot NVS
### [PixelNerf 2021](https://alexyu.net/pixelnerf/)
Nerf conditioned on feature volume.
![](/images/pixelnerf.png)

Nerf but other than normal 5d input, condition each point also on image features provided by the conditioned image (project nerf input point to image space on input image). This way the model learns to decode image features in 3d supervised by volume rendering constraint. Not very good result but seminal work.

> It's unclear why x is necessary as mlp input; possible explanation is they model the problem as conditional nerf i.e. radiance field conditioned on feature volume f(x,d; W(x))->(c, σ) so f is still a nerf. A better approach would be C(x,d): f(W(x),d)->(c, σ) which is used in most future work but this formulation is more similar to light field

### [Light Field Networks 2021 SL](https://www.vincentsitzmann.com/lfns/)
Light field conditioned on scene prior encoded from input image. 
![](/images/lfn.png)

Scene prior is necessary because 4d light field itself isn't 3d consistent (nerf addresses this problem by passing view direction late but light field can't separate its 4d inputs). 

> About light field: "Adelson et al. introduced the 5D plenoptic function as a unified representation of information in the early visual system. Levoy et al. and, concurrently, Gortler et al. introduced light fields in computer graphics as a 4D sampled scene representation for fast image-based rendering. Light fields have since enjoyed popularity as a representation for novel view synthesis and computational photography"

> More: "while the light field only encodes appearance explicitly, its derivatives encode geometry information about the underlying 3D scene"

> current formulation of LFNs does not outperform pixelNeRF. We note, however, that local conditioning methods solve a different problem. Rather than learning a prior over classes of objects, local conditioning methods learn priors over patches, answering the question “How does this image patch look like from a different perspective?”. As a result, this approach does not learn a latent space of neural scene representations. (Note that pixelNeRF does learn a latent space of feature volumes of neural scene representations. this paragraph is ambiguous in this sense but should be understood in a local patch encoding i.e. pixel aligned feature space perspective)

### [IBRNet 2021](https://ibrnet.github.io/)
![](/images/ibr.png)
![](/images/ibr2.png)

### [Light Field Neural Rendering 2022 Oral](https://light-field-neural-rendering.github.io/)
Light field formulation with epipolar feature aggregation and learned rendering function (both transformers). 
![](/images/nlf.png)


### [Generalizable Patch-Based Neural Rendering 2022 Oral](https://mohammedsuhail.net/gen_patch_neural_rendering/)
More complex than IBRNet (more transformers) but similar idea. Slightly better result than IBRNet
![](/images/gpnr.gif)

> ray representations (6d Plucker coordinates) are used as positional encoding in the transformers.

> 10 reference views and 20 depth points for training and evaluation

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
- 


## Generative
### [Generative NeRF](https://arxiv.org/abs/2007.02442)
Model p(x), where x is distribution of real 3d objects, with Gθ. Given shape and appearance prior, output a nerf representation of the 3d object. GAN training. 
![](/images/graf.png)
![](/images/graf1.png)

### [CLIP NeRF](https://arxiv.org/abs/2112.05139)
Feed forward generation. Given caption output a nerf representation of the described object. First train like GRAF with GAN loss, then fix conditional nerf model and train caption prior mapper with CLIP loss.

![](/images/clip-nerf.png)

> Note1: Used a deformation network to map points (position encodings) given shape encoding to displacement vector.

> Note2: "pre-trained CLIP model has the ability to support view-consistency representations for 3D-aware applications"


### [Dream Field](https://arxiv.org/abs/2112.01455)
Per caption optimization on nerf. 

### [Dream Fusion](https://arxiv.org/abs/2209.14988)
Per caption optimization on nerf. 
![](/images/dream-fusion.png)

 

### Misc.
#### [Queries on General Neural Implicit Surfaces](https://nmwsharp.com/research/interval-implicits/)
SIGGRAPH Best Paper
Difficult to convert Neural Implicit Surfaces to downstream representations (mesh, points...)

## Face
### [Dynamic Nerf for Monocular 4D Facial Avatar Reconstruction](https://arxiv.org/pdf/2012.03065.pdf)
-image->face expression latents->3d avatar
-training involves 

## Depth Prediction
### [MVSNet](https://arxiv.org/pdf/1804.02505.pdf)
- 2D CNN to generate 32-channel feature maps downsized by four in each dimension compared with input images (HxWx3->H/4xW/4x32)
- feature map projected (repeated) to 3d cost volume
- 3d U-net to determine occupanncy
- refine depth with initial reference image



--------------------------------------------
# Brain (NLP central)
## Memory
> My thinking: (this turns out to be exactly NTM) regard memory as a database. information generates key, query and value vectors. when new information comes, its query compares with key of all stored information. its value will be decoded and used as new query (thinking loop).  
### Storage
#### [NTM](https://arxiv.org/pdf/1410.5401.pdf)
- LSTM with external memory matrix. read and write memory like digital computer for each timestamp.
- What killed NTMs is that at the end of the day they're still recurrent networks, and thus inefficient and unstable to train in general.
- You don't need to have a external memory when you can apply attention to the whole input at once (sequential input is not really sequential when training).
- NTM as in program search is very interesting.
- Relationship with Transformer: ?

#### [Memory networks](https://arxiv.org/pdf/1410.3916.pdf)
concurrent with NTM but larger storage. tested mainly on question answering tests

#### [End-To-End Memory Networks](https://arxiv.org/pdf/1503.08895.pdf)
more with Memory networks

### Attention
#### [Neural machine translation by jointly learning to align and translate](https://arxiv.org/pdf/1409.0473.pdf)
Instead of decode from a fixed length encoding, keep all transformed embedding and selectively attend to those of interest. Intuition based.
