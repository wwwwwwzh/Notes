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
- Motivation: "the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder–decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly"
- Intuition: Decoder network receives a context vector at every decoding timestamp. This context used to be only from previous states and previous output/prediction. We want it to also depend on every word of input sequence and focus on the most relavent word (e.g. when translating from me gusta perros to I like dogs, "like" should see both me and gusta but particularly focusing on gusta). 

### Self Attention
<img width="700" alt="Screen Shot 2023-01-04 at 10 52 30 AM" src="https://user-images.githubusercontent.com/36484215/210618485-7ea28d20-7d98-4b20-b61e-9b2108bf1927.png">
- Intuition: for plain attention, every input should provide some relevant information and relevancy to every output. This can be done without RNN. 

### [Transformer](https://arxiv.org/pdf/1706.03762.pdf)
"A model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output."


# NLP & Vision -----------------------------------------
## Captioning


## Vision Transformer


# 3D ---------------------------------------------------
### [PointNet](http://stanford.edu/~rqi/pointnet/docs/cvpr17_pointnet_slides.pdf)
<img width="1000" alt="Screen Shot 2023-01-04 at 2 24 20 PM" src="https://user-images.githubusercontent.com/36484215/210652646-6a69efd5-b508-4a75-8166-88257994d5dd.png">

1. Global max pooling to enforce permutation invariance (points with different ordering should be the same scene)
2. Learned transformation to enforce invariance under geometric transformations (rotation)





