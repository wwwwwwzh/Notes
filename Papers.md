# Face
- [Unity The making of Enemies](https://www.youtube.com/watch?v=a0vAWyZXMWg&list=PLX2vGYjWbI0Q4rTRGHz9K71F4HnDUvGiF&index=2)
- [Ziva Face Trainer](https://zivadynamics.com/ziva-face-trainer)
- [Blender Facebuilder](https://medium.com/keentools/facebuilder-for-blender-guide-cbb10c717f7c)
- [Snap Face Mesh](https://docs.snap.com/lens-studio/references/templates/face/face-mesh#guide)

--------------------------------------------
# 2D Vision
## CNN
### Inside NN (https://youtu.be/gCJCgQW_LKc)
[Visualizing and Understanding Convolutional Networks](https://arxiv.org/pdf/1311.2901.pdf): 1) forward all images in dataset, find most activated activations, deconv to reconstruct, also find the original part of image. 2) saliency map (gradient of category score on each pixel) 3) occlusion sensitivity

<img width="600" alt="Screen Shot 2023-01-03 at 7 40 22 PM" src="https://user-images.githubusercontent.com/36484215/210474522-3916ad21-88f6-4372-95f9-41ea43c99db1.png">

> it seems that saliency map is not as good in object localization as specialized algorithms

### [Object Detection](https://www.coursera.org/learn/convolutional-neural-networks)
#### RCNN
- use selective search to extract just 2000 regions from the image and he called them region proposals.
- run CNN on each of the 2000 regions

#### [Yolo](https://arxiv.org/pdf/1506.02640.pdf)
<img width="400" alt="Screen Shot 2023-01-14 at 3 50 54 PM" src="https://user-images.githubusercontent.com/36484215/212498622-bb463112-e95f-4ac8-979b-f5476ba1376d.png">

<img width="400" alt="Screen Shot 2023-01-14 at 3 50 12 PM" src="https://user-images.githubusercontent.com/36484215/212498594-d42d85ee-d5f5-4d5c-b09d-3d55e66332bd.png">

## Image Generation
### Autoencoder
If encoder and decoder both have only one linear layer, this will result in a projection problem where projection hyperplane with minimal euclidean error is found. If we have a complex enough encoder decoder, it can essentially map every input to 1,2,3... and be able to reconstruct them.

### Variational Autoencoder
https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73

Plain autoencoders lack interpretable and exploitable structures in the latent space (lack of regularity) thus can't sample good images. This is because autoencoder is solely trained to encode and decode with as few loss as possible, no matter how the latent space is organized.

We want continuity (two close points in the latent space should not give two completely different contents once decoded) and completeness (for a chosen distribution, a point sampled from the latent space should give “meaningful” content once decoded).

Plain autoencoders overfit by either having low variance or making mean far from each other, thus we encourage the distribution to be normal.

![](/images/vae-reg.png)

### Diffusion
https://jalammar.github.io/illustrated-stable-diffusion/
Learn to remove noise.

### GPT
See transformer section below

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



--------------------------------------------
# Multimodal
## Image Captioning 
### Encoder-Decoder
#### Karpathy


### 
#### CLIP
![](/images/clip.png)

--------------------------------------------
# 3D Vision
## Scene Representation
### Occupancy Networks
implicitly represent the 3D surface as the continuous decision boundary of a deep neural network classifier. f(xyz, latent)->[0,1]. Can be used to do 3D reconstruction from single images, noisy point clouds and coarse discrete voxel grids. Loss=cross entropy between true occupancy and prediction + KL of latent code prior

### [PointNet](http://stanford.edu/~rqi/pointnet/docs/cvpr17_pointnet_slides.pdf)
<img width="1000" alt="Screen Shot 2023-01-04 at 2 24 20 PM" src="https://user-images.githubusercontent.com/36484215/210652646-6a69efd5-b508-4a75-8166-88257994d5dd.png">

1. Global max pooling to enforce permutation invariance (points with different ordering should be the same scene)
2. Learned transformation to enforce invariance under geometric transformations (rotation)

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
