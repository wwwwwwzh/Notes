## School Related
### Course Plan
- Visual or Performing Arts: APPL 110 (Introduction to Design and Making)
- Literary Arts: Cicero

### Interested
- ECON 415 Market Failure
- Hist 158 Early Modern Europe
- HIST 266 history of warfare
- HIST 315 NATION BUILDING LATIN AMERICA
- HIST 340 ETHICS AND BUSINESS IN AFRICA
- HIST 538 MIDDLE EAST & THE WEST


## Ideas
### Talk to make a world
basically auto game engine with ML to code stuff from what people tell them to do. everyone wants to create a world of their own and rule everything. dumb people can benefit from ML: engine ask conditions to make them exhaustive so ppl don't have to think of every cases.


### Linux Commands 
- df -h: view storage devices
- du -sh: view directory size
- scp -r /path/to/directory someuser@serverB:/path/to/files/: copies the directory itself into files folder
- cp -r ~/folder1/. ~/new_folder1: copies contents of folder1 to a new folder (will create if not exist)

-------------------------------------------------------------------------------------------------------------------------------

# Logs
## 12.19
### sherical harmonic 

<img width="200" alt="Screen Shot 2022-12-19 at 4 43 09 PM" src="https://user-images.githubusercontent.com/36484215/208555184-85d131f8-bfdd-402f-924f-b145467e3f6e.png">

ω = (sinθ*cosφ,sinθ*sinφ,cosθ)

basically a basis for sherical functions like fourier basis

### projection matrix (reviewing Roni's slides)
<img width="300" alt="Screen Shot 2022-12-19 at 5 24 44 PM" src="https://user-images.githubusercontent.com/36484215/208559444-a1df7cd3-3423-4590-8fa1-64dd07c854de.png">

Note that image plane doesn't change size

<img width="300" alt="focal length and ratio" src="https://user-images.githubusercontent.com/36484215/208560712-78b6cd10-949e-446a-8d1b-c3646280e610.jpg">

Note that when f→∞, this becomes orthographical projection and ratio will be 2.

## 12.20-22 (reading pbr book)
### BRDF
### Others
- [Mach bands](https://en.wikipedia.org/wiki/Mach_bands)
- Thor 4 is really bad. 
- Beam search in translation (balance between greedy search and resource constraint)
- Log is a really interesting function. When x is too big, it makes x grow slower. When x is too small, it makes x shrink slower. Everything is within a more controllable range. 

## 12.21
### Machine Translation
- statistical translation:
- [RNN encoder decoder](https://arxiv.org/pdf/1406.1078.pdf): "Unlike the traditional phrase-based translation system which consists of many small sub-components that are tuned separately, neural machine translation attempts to build and train a single, large neural network that reads a sentence and outputs a correct translation."
- [Attention](https://arxiv.org/pdf/1409.0473.pdf): "the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder–decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly"
- Self attention: replace RNN with dot product
- Transformer: more complex than I thought. wonder what intuition guided them

## 12.22-23
### PixelRNN
masked convolution + row LSTM to predict next pixel given all previous pixels

### GANS
#### GANS

#### DCGAN

#### [StyleGAN](https://arxiv.org/pdf/1812.04948.pdf)
the generators continue to operate as black boxes, and the understanding of various aspects of the image synthesis process, e.g., the origin of stochastic features, is still lacking. The properties of the latent space are also poorly understood, and the commonly demonstrated latent space interpolations provide no quantitative way to compare different generators against each other.

####

> Note: upsampling+conv is favored over transposed conv to avoid checkerboard artifacts. https://distill.pub/2016/deconv-checkerboard/

## 12.24-25
### Think
- Kanzi the ape
- koko the gorilla
- “The primate vocal tract is ‘speech ready,’ but ... most species don’t have the neural control to make the complex sounds that comprise human speech,” Dunn writes for The Conversation.
- Deaf people think in sign language or imagined sounds or visual stuff
- Blind people: echolocation, spatial understanding, other sensory information
- https://waitbutwhy.com/table/person-with-no-senses
- criticacl period for language (or really intelligence) development. Nervous system stops growing (real brain learning?)

Sensory or external stimuli is needed to start things. Curiosity and other premitive desires (survival, imitation, some are uniqu to individuals, some learned) to drive internal processing. Memory?
https://www.youtube.com/watch?v=mFP_AjJeP-M

#### Short term memory
- motivation1: when we see a particular shape for a long time, we might see everything as that shape. CNN analogy is every pass also keeps a weighted average of activation so if a particular activation shows up many times, a small activation there can be very big so it sees every image as containing that shape. 
- RNN: rnn is really that CNN analogy with trained retaining activation. Previous activations are kept alive when new input comes. 

#### Long term memory
- Motivation1: long term memeory should be stored to "empty new space", be queried with trained (possibly refinable) network. 
- KVQ query system. multiple Q what is this, is this dangerous, is this beautiful...
- google seems like a good memory system
- continuous refinement of memory by asking questions and creating new connections.

## 12.26-29
### Eating
Not eating after 12.25 dinner makes me starve early in the morning and feel bad throughout the day. Ate at 12.26 but still not good after 12.27 breakfast. Took a walk and ate lunch much better. Slept and all good. Ran short late afternoon. 28 morning stomach feeling funny 2p. 29 morning better 2p.  Ran afternoon.

### Math
- Group theory, spaces, review linear algebra
- Einstein notation
- Unconstrained optimization (f'=0 & positive definite Hessian) and why 1/2 for second order derivative (area of triangle)
- Constrained optimization (Lagrange multiplier)
- It seems that SVM is a more traditional way to do optimization but intuition guided neural network somehow is more flexible

