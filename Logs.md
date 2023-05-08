# Util/Tools
## Commands
### Linux Commands 
- conda env list
- conda list
- df -h: view storage devices
- du -sh: view directory size
- scp -r /path/to/directory zhw@hires-gpu1.cs.unc.edu:/playpen1/wzh/files/: copies the directory itself into files folder
- cp -r ~/folder1/. ~/new_folder1: copies contents of folder1 to a new folder (will create if not exist)
- screen -S "12917.tdnerf_baseline" -X sessionname "newname"
- tensorboard --logdir log; ssh -L 16006:127.0.0.1:6006 zhw@hires-gpu1.cs.unc.edu then go to http://127.0.0.1:16006: tensor board on ssh
- pstree / ps aux: show running processes

- jupyter notebook --no-browser --port=8080; ssh -L 8081:localhost:8081 zhw@hires-gpu1.cs.unc.edu

#### Tools
CMake: https://askubuntu.com/questions/829310/how-to-upgrade-cmake-in-ubuntu

### PyCharm Shortcut
select next occurrence: control + G 
deselect previous occurrence: shift + control + G 
copy line done: command + D

### VSCode Shortcut
copy line done/up: shift + opt + arrow
select next occurrence: command + D

### Git
https://learngitbranching.js.org/
- git commit
- git branch branchName
- git checkout branchName
- git checkout -b branchName
- git merge branchName
- git rebase branchName

#### Relative 
- git log
- git checkout commitHash
- git checkout branchName^
- git checkout HEAD^

- git reset --hard commitHash
- git reset HEAD~1
- git revert HEAD: new commit with content as previous commit. Use with pushed commits.

## Code
### Torch
```py
rearrange(x, "b (h c) x y -> b h c (x y)", h=heads) # from [b, c, x, y] to [b, h, c/h, x*y]
einsum("b h d i, b h d j -> b h i j", q, k) # if index is in result (b h i j), it's element to element; if index not in result: same index appear in both input matrices (d here): Einstein sum along that dimension (Σq[d]*k[d])
einsum("b h i j, b h d j -> b h i d", attn, v) 
```

## Websites
### ML
#### HuggingFace
https://huggingface.co/transformers/v2.9.1/pretrained_models.html: model name and size

### Language


### Others
https://www.letras.com/shakira/1657452/
----------------------------------------------------------

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

# Ideas
## School Related
### Course Plan
- Visual or Performing Arts: APPL 110 (Introduction to Design and Making)
- Literary Arts: Cicero

HS CI BN GL

### Interested
- ECON 231 Economic History of Western Europe
- ECON 234 Survey of the History of Economic Thought
- ECON 415 Market Failure
- Hist 158 Early Modern Europe
- HIST 266 history of warfare
- HIST 315 NATION BUILDING LATIN AMERICA
- HIST 340 ETHICS AND BUSINESS IN AFRICA
- HIST 538 MIDDLE EAST & THE WEST
- MUSC 120 Foundations in Music
- ARTH 151 History of Western Art I



## Projects
### Talk to make a world
basically auto game engine with ML to code stuff from what people tell them to do. everyone wants to create a world of their own and rule everything. dumb people can benefit from ML: engine ask conditions to make them exhaustive so ppl don't have to think of every cases.

### ML for Education
Find salient feature of things to teach. e.g. ni language, what's different and what's the same across and inter languages. Find easiest to remember and most important feature of the material.

## AI and Brain
### On Knowledge
> 20 years ago SVD (invented 1873) wasn't in linear algebra and 100 years ago no one use linear algebra.
Were they actively looking for and discovered ancient technics when they need more math to solve problems? How could they discover it? Did they use to know everything?

### On ML and optimization
To fit a function as complex as a DNN, some properties in the middle of the network have to emerge. If they are human understandable then it "learned" something.

### On local minima
Humans are prone to local minima. The physical configuration of human body admits infinite behaviors. Behaviors lead to consequences within their context. There are only finite context one will encounter. Thus many configurations will fit these seen contexts and people with "bad" configurations will believe they are smart such that they can solve problems they have seen. ML might be able to exhaust the data and learn a "true" good configuration (Roman+enlightenment?). 

### Learning from examples is superficial
Related to previous idea.

Create "inductive bias" as teaching more low level principles one at a time so it really understands things. Like in nerf where knowing geometry makes color optimization easier.

If we can "train a complete adult" model it will fulfill half of the quest. The problem is it's difficult to train. We need layered structure and train them one by one with appropriate tasks

### Early Neural Network Success
- 1989: Backpropagation applied to handwritten zip code recognition
- 1989: minimizing the number of free parameters in neural networks can enhance the generalization ability of neural networks
- 1996: Neural Network-Based Face Detection

> even though the problem (zip code) is linearly separable, single-layer networks exhibited poor generalization capabilities. When using shift-invariant feature detectors on a multi-layered, constrained network, the model could perform very well. He believed that these results proved that minimizing the number of free parameters in the neural network could enhance the generalization ability of the neural network.

### Misc
- artistic training during childhood change structure of brain forever and can't be done in adulthood?
- Neuron plasticity inspired SOM might work on very small tasks where all layers before are frozen and provide a solid inductive bias
- A brain should distinguish "self" from everything else. Emergent property of complex network?

## Movies to Watch
- The Last of the Mohicans
- Indiana Jones

## Quotes
### Talks
- Alan Kay on David Evans: Dave's way was to make something like a garden, and tend that garden so that many things would have many chance to grow by themselves. His idea was to just do good deeds everywhere and every time you can without any hope of return. And much of the time the angelic side of humans will nudge other humans to start helping themselves.
#### Hinton
- On intuition and knowledge distillation: you need to put in a lot of hard work to get sufficient experience in a domain and then you need to trust your intuitions. 
- On politics and science: I grew up in Britain in the 1950's and 60's and a major puzzle at the time was to understand how civilized and well-educated Germans could have allowed Hitler to gain power. Recent events in the US have made that seem a lot less puzzling. ... I believe that highly selected and extremely well-educated students like yourselves have a moral duty to stand up for the truth in the face of political attempts to suppress it.

### Books

### Forbes
- Bernard Arnault: I see myself as an ambassador of French heritage and French culture. What we create is emblematic. It's linked to Versailles, to Marie Antoinette.
- Elon Musk: I operate on the physics approach to analysis. You boil things down to the first principles or fundamental truths in a particular area and then you reason up from there.
- Jeff Bezos: I didn't think I'd regret trying and failing. And I suspected I would always be haunted by a decision to not try at all.
- Larry Ellison: When people start telling you that you're crazy, you just might be on to the most important innovation in your life.
- Bill Gates: Money has no utility to me beyond a certain point. Its utility is entirely in building an organization and getting the resources out to the poorest in the world.
- Carlos Slim Helu: When you live for others' opinions, you are dead. I don't want to live thinking about how I'll be remembered.
- Larry Page: You never lose a dream; it just incubates as a hobby.
- Sergey Brin: Obviously everyone wants to be successful, but I want to be looked back on as being very innovative, very trusted and ethical and ultimately making a big difference in the world.

### LATIN
- VIVAMUS MORIENDUM EST
- FORTIS FORTUNA ADIUVAT
- NIHIL SUB SOLE NOVUM
- SI VIS PACEM PARA BELLUM
- PER ASPERA AD ASTRA
- DUM SPIRO SPERO
- DUM VIVIMUS VIVAMUS
- ERRARE EST HUMANUM
- COGITO ERGO SUM
- CUI BONO
- ALEA LACTA EST
