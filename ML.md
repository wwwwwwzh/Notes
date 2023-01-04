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
