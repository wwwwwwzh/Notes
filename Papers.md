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

### Object Detection (https://www.coursera.org/learn/convolutional-neural-networks)
#### RCNN
- use selective search to extract just 2000 regions from the image and he called them region proposals.
- run CNN on each of the 2000 regions

#### [Yolo](https://arxiv.org/pdf/1506.02640.pdf)
<img width="487" alt="Screen Shot 2023-01-14 at 3 50 54 PM" src="https://user-images.githubusercontent.com/36484215/212498622-bb463112-e95f-4ac8-979b-f5476ba1376d.png">

<img width="795" alt="Screen Shot 2023-01-14 at 3 50 12 PM" src="https://user-images.githubusercontent.com/36484215/212498594-d42d85ee-d5f5-4d5c-b09d-3d55e66332bd.png">

# NLP
## RNN
### Inside RNN
#### [VISUALIZING AND UNDERSTANDING RECURRENT NETWORKS](https://arxiv.org/pdf/1506.02078.pdf)
"For instance, one cell is clearly acting as a line length counter, starting with a high value and then slowly decaying with each character until the next newline. Other cells turn on inside quotes, the parenthesis after if statements, inside strings or comments, or with increasing strength as the indentation of a block of code increases."

## Attention 
### Transformer


# 3D
## Vision
### Explicit 
#### Occupancy Networks
implicitly represent the 3D surface as the continuous decision boundary of a deep neural network classifier. f(xyz, latent)->[0,1]. Can be used to do 3D reconstruction from single images, noisy point clouds and coarse discrete voxel grids. Loss=cross entropy between true occupancy and prediction + KL of latent code prior
