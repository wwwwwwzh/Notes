# CNN
## Trend in Image Networks
### AlexNet 2012
### Inception 2014
### ResNet 2015
### DenseNet 2016

## Inside NN (https://youtu.be/gCJCgQW_LKc)
[Visualizing and Understanding Convolutional Networks](https://arxiv.org/pdf/1311.2901.pdf): 1) forward all images in dataset, find most activated activations, deconv to reconstruct, also find the original part of image. 2) saliency map (gradient of category score on each pixel) 3) occlusion sensitivity

<img width="600" alt="Screen Shot 2023-01-03 at 7 40 22 PM" src="https://user-images.githubusercontent.com/36484215/210474522-3916ad21-88f6-4372-95f9-41ea43c99db1.png">

> saliency map is not as good in object localization as specialized algorithms

## [Object Detection](https://www.coursera.org/learn/convolutional-neural-networks)
### RCNN
- use selective search to extract 2000 regions from the image as region proposals.
- run CNN on each of the 2000 regions

### [Yolo](https://arxiv.org/pdf/1506.02640.pdf)
<img width="400" alt="Screen Shot 2023-01-14 at 3 50 54 PM" src="https://user-images.githubusercontent.com/36484215/212498622-bb463112-e95f-4ac8-979b-f5476ba1376d.png">

<img width="400" alt="Screen Shot 2023-01-14 at 3 50 12 PM" src="https://user-images.githubusercontent.com/36484215/212498594-d42d85ee-d5f5-4d5c-b09d-3d55e66332bd.png">

## Object Segmentation
### [Mask-RCNN](https://arxiv.org/abs/1703.06870)
Summary: In addition to object class and bounding box, outputs binary mask to segment the object

# Generative ---------------
# Autoencoder
## Overview
https://lilianweng.github.io/posts/2018-08-12-vae/

Autocoder is invented to reconstruct high-dimensional data using a neural network model with a narrow bottleneck layer in the middle.

The encoder network essentially accomplishes the dimensionality reduction, just like how we would use Principal Component Analysis (PCA) or Matrix Factorization (MF) for

### Denoising Autoencoder
If encoder and decoder both have only one linear layer, this will result in a projection problem where projection hyperplane with minimal euclidean error is found. If we have a complex enough encoder decoder, it can essentially map every input to 1,2,3... and be able to reconstruct them. This is also overfitting.

This design is motivated by the fact that humans can easily recognize an object or a scene even the view is partially occluded or corrupted.

For high dimensional input with high redundancy, like images, the model is likely to depend on evidence gathered from a combination of many input dimensions to recover the denoised version rather than to overfit one dimension. This builds up a good foundation for learning robust latent representation.

![](/images/denoising-autoencoder-architecture.png)

### Other Robustness Improving Models
- Sparse autoencoder: It forces the model to only have a small number of hidden units being activated at the same time, or in other words, one hidden neuron should be inactivate most of time. Done with a KL loss on bernoulli of activate or not.
- k-Sparse Autoencoder: only k top activated neurons of z is kept so backprop only through those neurons
- Contractive Autoencoder: penalize the representation being too sensitive to the input, and thus improve the robustness to small perturbations around the training data points. The sensitivity is measured by the Frobenius norm of the Jacobian matrix of the encoder activations with respect to the input

## Variational Autoencoder
### [Intuition](https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73)
Plain autoencoders lack interpretable and exploitable structures in the latent space (lack of regularity) thus can't sample good images. This is because autoencoder is solely trained to encode and decode with as few loss as possible, no matter how the latent space is organized.

We want continuity (two close points in the latent space should not give two completely different contents once decoded) and completeness (for a chosen distribution, a point sampled from the latent space should give “meaningful” content once decoded).

Plain autoencoders overfit by either having low variance or making mean far from each other, thus we encourage the distribution to be normal.

![](/images/vae-reg.png)

### Variational Inference (real motivation for VAE)
Images are projection of their underlying structures (latent). So the real world generation of image is always graphical: from z to x. Want to find this relationship to learn p(x)

1. want argmaxΣlogpθ(x) where x is real data
2. pθ(x)=∫p(x|z)p(z)dz which is intractable
3. instead of computing p(x|z)p(z) for every z, estimate p(z|x) and compute p(x) by sampling from estimated z distribution, 

For computing loss:
1. want to minimize KL(q(z|x)|p(z|x))
2. equivalent to maximizing ELBO
3. See Statistics note for complete derivation

![](/images/vaeLoss.png)
ELBO can be further decomposed into 2 terms which correspond to a reconstruction and prior matching term. 
![](/images/vaeIntuition.png)

### Hierarchical VAE
Latent variables themselves are interpreted as generated from other higher-level, more abstract latents.

In addition to layers of latent variables, treat the conditional generation process as a markov process so Zt only depends on Zt+1. The joint distribution is then:
$p(x, z_{1:T}) = p(z_T)p_{\theta}(x\mid z_1)\prod_{t=2}^{T}p_{\theta}(z_{t-1}\mid z_{t})$

Posterior:
$q_{\phi}(z_{1:T}\mid x) = q_{\phi}(z_1\mid x)\prod_{t=2}^{T}q_{\phi}(z_{t}\mid z_{t-1})$

## VQ-VAE
learns a discrete latent variable by the encoder

# [GANs](https://lilianweng.github.io/posts/2017-08-20-gan/)
https://colinraffel.com/blog/gans-and-divergence-minimization.html

Problem of generative modeling:
- Minimizing Forward KL is equivalent to MLE, but it tries to cover all the mode (since the log(p/q) term becomes infinite when p!=0 and q->0) 
- Minimizing Backward KL is equivalent to maximizing entropy of q and second is log probability of samples from qθ(x) under the true distribution p(x)

Objective:
![](/images/gan.png)

Propositions:
1. For G ﬁxed, the optimal discriminator D is $D^*_G(x)=\frac{p_{data}(x)}{p_{data}(x)+p_g(x)}$.
This can be proved for V=the chosen objective with the fact that the function f: y → a⋅log(y) + b⋅log(1 − y) achieves its maximum in [0, 1] at a/(a+b). Since D(x) can be interpreted as estimating P(from data or not|x), optimal D assigns 1 to image certainly from data and certainly not from generator, 0 to certainly not from data and 0.5 to equally likely from either.
2. The global minimum of the virtual training criterion C(G) is achieved if and only if p g = p data . At that point, C(G) achieves the value − log 4.
![](/images/ganV.png)
![](/images/ganJSD.png)
This means given an optimal discriminator, the generator tries to minimize the JSD of pdata and pg which moves pg to pdata and at which time minimum of -log4 is achieved.

Conclusion:
The alternating minimax objective can be seen as divergence minimization but the divergence is given by the discriminator. The whole process first makes the divergence more accurate (discriminator training) then minimizes it (generator training) then repeat until generator describes the true divergence.

[Question]: Can JSD be interpreted as expectation of cross entropy of discriminator P(y|x) and true P(y|x)?


## [Progressive GANs](https://arxiv.org/pdf/1710.10196.pdf)
![](/images/progGAN.png)
## StyleGAN
![](/images/styleGAN.png)
![](/images/styleGAN2.png)

## Image Translation
### [Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/abs/1611.07004)
Apply Conditional GANs on many image to image generation problems.

### [Multimodal Unsupervised Image-to-Image Translation](https://arxiv.org/abs/1804.04732)
Problem: image mapping (sketch to image, colorization, style transfer...) or translating image to another domain (p(x'|x)) is multimodal but existing approaches assume a deterministic or unimodal mapping.

Solution: uniform content space but different style space to approximate this multimodal distribution.

![](/images/multimodal-itoi.png)
![](/images/multimodal-itoi2.png)

# Diffusion
## Overview
- https://jalammar.github.io/illustrated-stable-diffusion/
- https://huggingface.co/blog/annotated-diffusion
- https://yang-song.net/blog/2021/score/

A (denoising) diffusion model is like other generative models such as Normalizing Flows, GANs or VAEs: they all convert noise from some simple distribution to a data sample. Diffusion model learns to gradually denoise data starting from pure noise.

### [Score Matching Perspective](https://arxiv.org/abs/1907.05600)
> a new generative model where samples are produced via Langevin dynamics using gradients of the data distribution estimated with score matching. ... Crucially, we train a single score network conditioned on the noise level and estimate the scores at all noise magnitudes

In traditional generative models like VAE or autoregressive models, we model probability density function over input data to approximate true data distribution (probability of all images). This results in intractable normalizing constant. So we instead learn a *score function* defined as gradient of log of probability density function. We can learn this by score matching.

Once we have the score function, we use Langevin dynamics which provides an MCMC procedure to sample from distribution p(x)

![](/images/score-multi-density.png)
First problem for naive implementation is inaccurate score for low density region since we don't have many samples to learn from. Our solution is to perturb data points with noise and train score-based models on the noisy data points instead.

In addition, we use multiple scales of noise perturbations simultaneously. we estimate the score function of each noise-perturbed distribution. Then we can train a Noise Conditional Score-Based Model.

> The manifold hypothesis states that data in the
real world tend to concentrate on low dimensional manifolds embedded in a high dimensional space (a.k.a., the ambient space).

### [Thermodynamics Perspective](https://arxiv.org/abs/2006.11239)

> a certain parameterization of diffusion models reveals an equivalence with denoising score matching over multiple noise levels during training and with annealed Langevin dynamics
during sampling

### Comparison with Other Generative Models
- Comparison with denoising autoencoder: similar except for variable timestep conditioning. Similar result on toy example can be achieved with both models. "Diffusion decomposes the image formation process into a sequential application of denoising autoencoders."

### The model:
- Overview: the network takes a batch of noisy images of shape (batch_size, num_channels, height, width) and a batch of noise levels of shape (batch_size, 1) as input, and returns a tensor of shape (batch_size, num_channels, height, width)
1. a convolutional layer is applied on the batch of noisy images, and position embeddings are computed for the noise levels
2. a sequence of downsampling stages are applied. Each downsampling stage consists of 2 ResNet blocks + groupnorm + attention + residual connection + a downsample operation
3. at the middle of the network, again ResNet blocks are applied, interleaved with attention
4. next, a sequence of upsampling stages are applied. Each upsampling stage consists of 2 ResNet blocks + groupnorm + attention + residual connection + an upsample operation
5. finally, a ResNet block followed by a convolutional layer is applied.


### Math
$$q(\mathbf{x}_t \vert \mathbf{x}_{t-1}) = \mathcal{N}(\mathbf{x}_t; \sqrt{1 - \beta_t} \mathbf{x}_{t-1}, \beta_t\mathbf{I}) \quad
q(\mathbf{x}_{1:T} \vert \mathbf{x}_0) = \prod^T_{t=1} q(\mathbf{x}_t \vert \mathbf{x}_{t-1})$$
Reparametrize:
$$\begin{aligned}
q(\mathbf{x}_t \vert \mathbf{x}_0) &= \mathcal{N}(\mathbf{x}_t; \sqrt{\bar{\alpha}_t} \mathbf{x}_0, (1 - \bar{\alpha}_t)\mathbf{I})
\end{aligned}$$

## Conditional Diffusion
In the conditional generation setting, the data x0 has an associated conditioning signal c. The only modification that needs to be made is to inject c as a extra input to the neural network function approximators: instead of µθ(xt, t) we now have µθ(xt, t, c), and likewise for Σθ. The particular architectural choices for injecting these extra inputs depends on the type of the conditioning c

## [Guidance](https://sander.ai/2022/05/26/guidance.html)
Conditional generative models model p(x|y) and in diffusion case is proportional to p(x)+p(y|x) where p(y|x) could be a normal classifier. In practice score from unconditional diffusion model and gradient of a classifier are combined to update current image. However, this classifier needs to be trained on noisy image so can't use pretrained ones.

In classifier free guidance, an unconditional diffusion model and a conditional diffusion model are trained jointly with a single network. The barycentric combination of these two models are used to update current image.



### [Stable Diffusion/Latent Diffusion](https://arxiv.org/abs/2112.10752)
![](/images/stable-diffusion.png)

- x is image and E is a pretrained frozen image encoder, the image is paired with things on the right (conditioning)
- Diffusion on latent space (auto-encoder) "training diffusion models on such a representation allows for the first time to reach a near-optimal point between complexity reduction and detail preservation"
- OpenClip encoding of text added to all attention layers at every time step. 
- Cross attention from image and text encoding (Q: image, K,V: text)

# Image Transformer
## [Image GPT](https://openai.com/blog/image-gpt/)
Directly use gpt on pixels. Tested both autoregressive and bert like training.

![](/images/igpt.png)

## [Vision Transformer](https://arxiv.org/pdf/2010.11929.pdf) 
Vision Transformer has much less image-specific inductive bias than CNNs. In CNNs, locality, two-dimensional neighborhood structure, and translation equivariance are baked into each layer throughout the whole model. In ViT, only MLP layers are local and translationally equivariant, while the self-attention layers are global

![](/images/ViT.png)

## [BEiT: BERT Pre-Training of Image Transformers](https://arxiv.org/pdf/2106.08254.pdf)
BEiT models are regular Vision Transformers, but pre-trained in a self-supervised way rather than supervised. Note iGPT doesn't employ vision specific processing like using image batch or targeting discrete visual tokens

The BEIT pre-training can be viewed as variational autoencoder training

![](/images/BeIT.png)

## [DALL·E](https://openai.com/blog/dall-e/)
DALL·E is a simple decoder-only transformer that receives both the text and the image as a single stream of 1280 tokens—256 for the text and 1024 for the image—and models all of them autoregressively.
1. train a discrete VAE (256^2->32^2)
2. concatenate up to 256 BPE-encoded text
tokens with the 32 × 32 = 1024 image tokens, and
train an autoregressive transformer to model the joint
distribution over the text and image tokens.

## [DALL·E 2](https://arxiv.org/pdf/2204.06125.pdf)
Train a prior that generates a CLIP image embedding given a text caption, and a decoder that generates an image
conditioned on the image embedding (diffusion)
