# Face
- [Unity The making of Enemies](https://www.youtube.com/watch?v=a0vAWyZXMWg&list=PLX2vGYjWbI0Q4rTRGHz9K71F4HnDUvGiF&index=2)
- [Ziva Face Trainer](https://zivadynamics.com/ziva-face-trainer)
- [Blender Facebuilder](https://medium.com/keentools/facebuilder-for-blender-guide-cbb10c717f7c)
- [Snap Face Mesh](https://docs.snap.com/lens-studio/references/templates/face/face-mesh#guide)

# CNN
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

## Attention 
### Transformer

# Multimodal
## Image Captioning 
### Encoder-Decoder
#### Karpathy


### 

# 3D
## Vision
### Explicit 
#### Occupancy Networks
implicitly represent the 3D surface as the continuous decision boundary of a deep neural network classifier. f(xyz, latent)->[0,1]. Can be used to do 3D reconstruction from single images, noisy point clouds and coarse discrete voxel grids. Loss=cross entropy between true occupancy and prediction + KL of latent code prior

### Depth Prediction
#### [MVSNet](https://arxiv.org/pdf/1804.02505.pdf)
- 2D CNN to generate 32-channel feature maps downsized by four in each dimension compared with input images (HxWx3->H/4xW/4x32)
- feature map projected (repeated) to 3d cost volume
- 3d U-net to determine occupanncy
- refine depth with initial reference image

# Brain
## Memory
> My thinking: regard memory as a database. information generates key, query and value vectors. when new information comes, its query compares with key of all stored information. its value will be decoded and used as new query (thinking loop).  
### [NTM](https://arxiv.org/pdf/1410.5401.pdf)
- LSTM with external memory matrix. read and write memory like digital computer for each timestamp.
- What killed NTMs is that at the end of the day they're still recurrent networks, and thus inefficient and unstable to train in general.
- You don't need to have a external memory when you can apply attention to the whole input at once (sequential input is not really sequential when training).
- NTM as in program search is very interesting.
- Relationship with Transformer: ?
