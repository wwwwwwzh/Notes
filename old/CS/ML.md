# History
## Connectionism 1873
https://youtu.be/VO5vKowfMOQ
- Associationism
- Connectionism: both functions and memories are encoded in the connections of neurons 
- Alexander Bain 

## Mathematical Modal of Brain
- McCulloch and Pitts model 1943: Threshold unit. Mathematical model of brain based on multiple excitatory dendrites and one inhibitory dendrite and one axon. Didn't provide learning algorithm.
- Hebbian Learning 1949: Neurons that fire together wire together. However initial model was unbounded, this leads to Sanger's rule

## Perceptron 1958


### Overview
Modified McCulloch and Pitts model. Single layer weighted sum of inputs. Can only learn linearly separable tasks.

### Learning
Add or subtract value of x. Since wx > T or < T, wx=T (T for threshold) is the line separating good and bad weights. X is the normal vector of that line so going in the direction of x guarantees better weight. This is equivalent to backprop with binary cross entropy (non-logged) loss.

### Minsky & Papert 1968


## Symbolic AI
https://www.cs.toronto.edu/~hinton/HintonMumbai.pdf

I think the whole history of AI might have been quite different if the two major figures who believed in neural nets in the 1950's had not died before their time. One was Alan Turing and the other was John von Neumann. Neither of them could be accused of being ignorant of logic, but they were both convinced that it was not the way to understand how the brain computed.

The rejection of neural networks was even more vociferous in the school of linguistics led by Noam Chomsky. I remember watching a TV program called Nova about linguistics. One after another, the leading linguists of the day looked straight at the camera and said that there was a lot we do not know about language, but one thing we know for sure is that it is not learned.


# Motivation of DNN
### Weight Optimization VS Error Optimization
Old perceptron learning algorithms guarantees to make weight closer to good weight space (if it exists) every iteration. Delta rule learning makes residual error smaller.  

The linear case of perceptron learning and chain rule error minimization can be connected:
![](/images/perceptron-backprop.png)
![](/images/weight-space.png)

## Motivation of Backprop
https://youtu.be/VCT1N0EsGj0?t=313
1. Perceptron features->hidden neurons: perceptron learning requires good features but they come from trial and error; want a way to automatically learn features 
2. Evolution algorithm (randomly perturb weights) is inefficient
3. Instead we could perturb activities since there're fewer neural activities than weights, but still inefficient
4. Backprop gives us change of error wrt activities.

### Learning Ability (Backprop paper)
In the family tree learning example, the network is capable of producing weights that exhibit human like reasoning behavior. For example, one neuron has weights such that it outputs 1 for English people and 0 for italian. 

![](/images/family-leanring.png)
![](/images/family-leanring2.png)


# Bayesian Learning
> W is weight and D is data
## MAP & Weight Decay
![](/images/mse-gaussian.png)
![](/images/map-wd.png)

## Full Bayesian Learning
Find the full posterior distribution P(W|D) and make predictions based on expectation of P(y|x, W).

$p(y|x, D)=\sum_i p(W_i|D)\cdot p(y|x, W_i)$

### MCMC
p(W|D)∝p(D|W)⋅p(W)

So when we use backprop on L₂ regularized maximum likelihood, the update vector is gradient of log(p(W|D)) and when we do random walk with this gradient, we'll get samples with sample density in proportion to p(W|D)

## Dropout
Dropout can be seen as combining many large NN models (different model for every training case). 

Original motivation was to fight collaboration of experts. Individual neurons tend to co-adapt to later neurons since they update residual gradient backproped from later layers.

# Hopfield Network
## Overview
Recurrent network where given initial input (partial memory) that settles at local energy minima which represents memorized patterns (associative memory)

## Evolution
### Rule
Local field of yᵢ is Σwᵢⱼyⱼ which is sum of influence of all neighboring nodes (all nodes except itself). For every update, we want sign(yᵢ)=sign(Σwᵢⱼyⱼ). This means that yᵢ is determined by other nodes. This mimics a MLP where the threshold function outputs 1 or -1 for x>0 or ≤0.  

### Energy
This is originally inspired by spin glass but here we deduce the energy function in a hindsight way. 

We want a function E of the network N, where N is represented by all its weights and output of all nodes, st D is lowest when the aforementioned rule no longer changes the network, i.e. sign(yᵢ)=sign(Σwᵢⱼyⱼ) ∀i. A simple way is to find something that increases whenever a node is forced to break the rule. 

Observe that when we break the rule for a node yᵢ⁻, it becomes -yᵢ⁻. Denote this yᵢ⁺. yᵢ⁻(Σwᵢⱼyⱼ) is positive. yᵢ⁺(Σwᵢⱼyⱼ) = -yᵢ⁻(Σwᵢⱼyⱼ). So yᵢ⁺(Σwᵢⱼyⱼ)-yᵢ⁻(Σwᵢⱼyⱼ)=-2yᵢ⁻(Σwᵢⱼyⱼ) which is always negative. Thus we have found a function of the network that always decrease from the optimum point that matches the rule. D=Σyᵢ(Σwᵢⱼyⱼ) is a more general version. 

Define E=-Σwᵢⱼyᵢyⱼ which is -D. E reaches minimum when the rule is satisfied. This is multiplied by a factor of 0.5 as explained in the next section.

In matrix form E=-0.5Y^TWY

### Spin Glass
Total energy of the system: 

## Learning
To store N bits, need N neurons. Want to find N(N-1)/2 weights of this network where values of neurons evolve to desired values.

This means these values wrt energy function has to be stable and stationary.

### Hebbian
1. Stationary: sign(Σwᵢⱼyⱼ)=yᵢ This is satisfied with Hebbian Learning where wᵢⱼ=yᵢyⱼ. 
![](/images/hn-station.png)
2. Stable:
![](/images/hn-stable.png)

### Multiple Patterns


# Misc
## Mixture of Experts
Data has multiple regimes (i.e. maybe there's a hidden input variable that determines the relationship between seen inputs and outputs). Sometimes this means data looks multimodal






























OLD-------------
# CNN
## Inside CNN
### Activation
Activations are images in another lower dimensional space and can be related somewhat easily back to original image.
- For the first several layers the activation is human readable images highlighting things like edges, corners, cirles, etc.
- For later layers activation maps become more abstract. A face image might be transformed into a small activation with a white pixel in the middle indicating a face there.
- Final activations are many small images each indicating if there is some abstract objects in the original image and where are they. For example, a face image might become several hundred 3x3 images indicating location of mouth, shirt, hair, eyes, etc. These abstract things are learned to facilitate tasks trained on the network and can go beyond the categories labeled (a library label might create recognition of texts in the image even though not explicitly trained on)
- These final activations are like those hand engineered features. Given these clever features later tasks can use relatively simpler network to convert to other outputs

### Filter
- Filters from the first layer are similar to those used in traditional CV. 
- Filters learn to create increasingly abstract features. This is because the same grid of pixels from later activations contains information about a wider receptive field.

### Reconstruction from Activation
To get reconstruction of a feature/activation map: forward all images in dataset, find most activated activations, deconv to reconstruct, also find the original part of image.

<img width="600" alt="Screen Shot 2023-01-03 at 7 40 22 PM" src="https://user-images.githubusercontent.com/36484215/210474522-3916ad21-88f6-4372-95f9-41ea43c99db1.png">

## Applications
### [YOLO](https://arxiv.org/pdf/1506.02640.pdf)
<img width="600" alt="Screen Shot 2023-01-04 at 9 23 07 AM" src="https://user-images.githubusercontent.com/36484215/210601513-f2f720dc-611b-48e9-998b-ae5dee07cc98.png">
<img width="600" alt="Screen Shot 2023-01-04 at 9 25 45 AM" src="https://user-images.githubusercontent.com/36484215/210602070-68da2fc8-800d-440d-bdda-f1cf31fb9d07.png">

1. image go through many conv layers to get a grid of features. This is essentially sliding window but much faster than doing all the conv for each window
2. each feature contains probability of detection, bounding box, and class of object
3. IOU and Non-Max suppression to get final bounding boxes.
4. Note that each grid sees more than the grid itself




# NLP -------------------------------------------------
## Attention & Transformer
### Attention


### Self Attention
<img width="700" alt="Screen Shot 2023-01-04 at 10 52 30 AM" src="https://user-images.githubusercontent.com/36484215/210618485-7ea28d20-7d98-4b20-b61e-9b2108bf1927.png">
- Intuition: for plain attention, every input should provide some relevant information and relevancy to every output. This can be done without RNN. 

### [Transformer](https://arxiv.org/pdf/1706.03762.pdf)
"A model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output."


# NLP & Vision -----------------------------------------
## Captioning


## [Vision Transformer](https://arxiv.org/pdf/2010.11929.pdf)


# 3D ---------------------------------------------------
### [PointNet](http://stanford.edu/~rqi/pointnet/docs/cvpr17_pointnet_slides.pdf)
<img width="1000" alt="Screen Shot 2023-01-04 at 2 24 20 PM" src="https://user-images.githubusercontent.com/36484215/210652646-6a69efd5-b508-4a75-8166-88257994d5dd.png">

1. Global max pooling to enforce permutation invariance (points with different ordering should be the same scene)
2. Learned transformation to enforce invariance under geometric transformations (rotation)








