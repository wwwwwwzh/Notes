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
- https://fluent-forever.com/product/fluent-forever-pronunciation-trainer/
- [Alphabet: The origin of every letter](https://www.youtube.com/watch?v=CYqqFqoLnnk)
- [Cyrillic Alphabet](https://www.youtube.com/watch?v=5kDpO9T-z60)

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

## 23.7.14-20
Ate salmon 7.14, diarrhea 7.15 but generally feel good. 7.16 went out and all good ate few for dinner. 7.17 very hungry in the morning and hungry though the day. 7.18 played badminton feel good and ate a lot. 7.19 feel good. 7.20 a little nervous and don't feel like eating breakfast but good throughout day.

# Ideas
## School Related
### Course Plan
- Visual or Performing Arts: APPL 110 (Introduction to Design and Making)
- Literary Arts: Cicero

HS CI BN GL

### Interested
- ECON 231 Economic History of Western Europe
- ECON 234 Survey of the History of Economic Thought

- ARTH 151 History of Western Art I

- NSCI 222 - LEARNING
- NSCI 423 - NEUROTECHNOLOGY
- NSCI 421 - PRINCIPLES OF BRAIN CIRCUITS
- NSCI 434 - COGNITIVE NEUROSCIENCE

- ECON 415 Market Failure
- Hist 158 Early Modern Europe
- HIST 266 history of warfare
- HIST 315 NATION BUILDING LATIN AMERICA
- HIST 340 ETHICS AND BUSINESS IN AFRICA
- HIST 538 MIDDLE EAST & THE WEST
- MUSC 120 Foundations in Music




## Projects
### Talk to make a world
basically auto game engine with ML to code stuff from what people tell them to do. everyone wants to create a world of their own and rule everything. dumb people can benefit from ML: engine ask conditions to make them exhaustive so ppl don't have to think of every cases.

### ML for Education
Find salient feature of things to teach. e.g. ni language, what's different and what's the same across and inter languages. Find easiest to remember and most important feature of the material.

### Universal Linker
Just like how brain links information from different modalities, note taking should focus on relations. e.g. drag a page on pdf to become a link just like url, everything on any software should have a unique location marker for reference.

## AI and Brain
### On Knowledge
> 20 years ago SVD (invented 1873) wasn't in linear algebra and 100 years ago no one use linear algebra.
Were they actively looking for and discovered ancient technics when they need more math to solve problems? How could they discover it? Did they use to know everything?

#### Knowledge Map
It's useful to connect everything to everything else but that requires n^2 computaion. Even future AI can't do it. But in the case of scenary information, we know how every location relates to every other location and we know how to go from anywhere to anywhere with little thinking. It's because we have a map that gives us overall view of everything. Manifold learning is thus important.

### On What is Learning When ML is Just An Optimizer
To fit a function as complex as a DNN, some properties in the middle of the network have to emerge. If they are human understandable then it "learned" something. This is also the thought of Hinton and what he convinced the Nature reviewer with.

### On Consciousness, Evolution and Optimization
We do a lot of amazing things, but animals can also do most of them. It's important to identify things that truly make us superior. I think I'll just define those properties as "high consciousness". Through evolution, animals began to have interesting traits and behaviors that offer evolutional advantages. Through kin selection and corporation they can even naturally develop behaviors that optimize complex games like war and social hierarchy. To empower these actions, animal brains must be powerful. We can see animals perform human like behaviors like doing chores and trade. These are not consciousness though. Currently I think language and symbolic thinking is key to consciousness as they establish a clear information flow inside brain (see quotes from The Story of My Life). 

https://www.perkins.org/laura-bridgman/

### Reading The Story of My Life (Helen Keller)
- > At first, when my teacher told me about a new thing I asked very few questions. My ideas were vague, and my vocabulary was inadequate; but as my knowledge of things grew, and I learned more and more words, my field of inquiry broadened, and I would return again and again to the same subject, eager for further information. Sometimes a new word revived an image that some earlier experience had engraved on my brain.

### On Logical and Natural Optimization/Why Our Logical Strategies Coincide Natural Phenomena
We see tit for tat in animals even when this is also deduced from human analytical thinking. We see learning algorithms reach local minima when human also reach local minima with the exact logic i.e. it looks good from where I came from and without an external nudge this will always be the best solution I can see. This is because systems have to follow the same physical laws and their high level behaviors have to sometimes follow patterns to satisfy those laws.

### On local minima
Humans are prone to local minima. The physical configuration of human body admits infinite behaviors. Behaviors lead to consequences within their context. There are only finite context one will encounter. Thus many configurations will fit these seen contexts and people with "bad" configurations will believe they are smart such that they can solve problems they have seen. ML might be able to exhaust the data and learn a "true" good configuration (Greco-Roman+bad time?). 

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

## Advanced AI and Brain
### What Counts as Output (Consciousness)
Since we don't know how consciousness arises,we don't know if it's the spatial or temporal activations of certain neurons or a certain pattern of transmission of potentials that matters as desired output of a network.

### Modeling Relationship Between Interesting Neurons
We can find certain neurons that's activated by certain things but we don't know connections between these neurons. To study how information is processed, we must either identify all connection strength between neurons of interest or build statistic models to measure how different "metaneurons" relate to each other.

### Function of Hippocampus as Associative Center


### Infinite Memory
If "one memory" corresponds to a pattern of activations of certain neurons, then given infinite connection complexity, different inputs (senses) can leads to (recall) 2^n memories. 

#### Problem of Null Memory
If recalling of memory means reading from a certain groups of neurons, then attempting to recall when given non recallable inputs should theoretically be still possible and would yield some random memory. But this didn't happen. For example, reading books read before gives some feeling of knowing stuff ahead but reading new books doesn't, though some activities have to be happening at the same region activated in the former event.

### Misc
- We can sometimes remember if we have recalled a memory or not 
- What happens in dream can be as influential as reality and thus more powerful than imagination

### Recurrent Connections
Two way information processing means two way learning (e.g. an image -> an idea + the idea -> the image)

### Horizontal Connections
Recurrent horizontal connections can be converted to hopfield network

## On Projection
### The World as Projection of an Underlying Structure and Every Natural Science as Projection Problem

### Logic as an Infallible Structure of the World

### Math as THE structure / Language of the Universe

Math provides language for the structure of things. When we see things happen, we first try to reason abstractly the underlying force that drives the happening. This is abstract. To prove something to be true, a language infinitely precise is needed. With this language can we really say this force produced such results.

See "Math and Physics" for whether math itself provides the structure.

### Math and Physics
It seems that primitive math emerges everywhere out of basic needs and grows as economy of the region. However, once physics is born, math becomes tool of physics. 

However, in a different lens, math is a desire to precision, and it inevitably leads to reduction to some extremely primitive and precise/self evident postulates. This is similar to physics's attempt to find something basic that explains everything complex. It also follows from these postulates that 

## Metaphysics
### On Logic
Since I feel Plato's idea of form is nonsense, I was trying to prove how every idea is derived from senses. It's easy to see that numbers have some clear physical meanings: two object normally result in two complete contours; two sounds are separated or differentiated naturally. However, logic seems more mysterious. Logic like parallel line postulate doesn't correspond to physical things that have clear boundaries. It is from some precise definitions that live on their own. Processing of them doesn't elicit sense memories but is a byproduct of some functions of brain. It's also possible that the most primitive logic are indeed generalizations of senses. For example:
![](/images/common-notions.png)
These are completely from senses. And from such generalizations we can build prepositional logic and others. So are also for numbers like: 1-A unit is that by virtue of which each of the things that exist is called one. 2-A number is a multitude composed of units.

![](/images/postulates.png)



### Ontology
#### Existence of Idea
I have an idea of a car because I've seen and rode a car and sensed it with all my sense organs. But does the idea exist by its own, i.e. If there are no humans, do cars exist?

Some people believe that these physical things, these "matter" are always real regardless of observation. However, a more difficult case would be something like this: a program exists because I have written it and run it, but I know there are infinitely many programs that "exist" but are yet to be written. We might solve this by having different levels of existence (exist now, past, future). 

But what about pure ideas? What about the relationship between a circle and its radius? The relationship never changes. But does it exist without being discovered?

## History
### Assumptions
- What happens if Medieval is skipped (Rome conquered all of Europe and slavs)

### Comparative
- Why Muslin golden age didn't produce Enlightenment and Scientific Revolution
- Different paths Mediterranean and China took in ancient times
- Compare China with Europe after Rome before Modern Era
- What exactly powered the train of Renaissance to Industrial Revolution
- What's lacking in Chinese and Islamic science compared to European science.
- How is communism different from "good" colonialism.

### 
- Why didn't Rome continue Greek legacy

## General
### 
- The language of literature is too full of emotions and experience that only looking back at the words as your own memories can you truly understand; the language of political philosophy is too full of hate and beliefs, understanding them is thus to become a cult; only the language of science is impartial, it stands above feelings and senses. 
- People don't have a sense of time yet they care about ideas like "recently" "not long ago" "long time ago" "ancient". As long as they are not born at that time, it doesn't matter to them if you describe a time period as 10 years, 100 years, or 1000 years ago. Lack of historical integrity.
- Number 3 is very interesting. When we see things the second time, we are excited because we can recognize it, but when we see it the third time, we sense a pattern. Also Taoism says everything is from 3. Also the cocktail treatment use combination of 3 drugs. Triangle has 3 sides and is most stable...

## Pedagogy
### Why Learn Everything with History
It is most natural to learn things from historical perspective. True learning comes from answering questions asked by oneself. The questions arise naturally given historical context since it's that exact same context that prompted people to ask the question that leads to the solution we are trying to learn. The answers also lock tightly with the historical question since we are all humans having essentially similar processes of innate minds.


## Movies to Watch
- The Last of the Mohicans
- Indiana Jones

## Quotes
### Books
### Heisenberg
- On physics and philosophy: My mind was formed by studying philosophy, Plato and that sort of thing". "Modern physics has definitely decided in favor of Plato. In fact the smallest units of matter are not physical objects in the ordinary sense; they are forms, ideas which can be expressed unambiguously only in mathematical language"

#### Da Vinci
- On flight (not really from him): When once you have tasted flight, you will forever walk the earth with your eyes turned skyward. For there you have been, and there you will always long to return

#### Einstein
- On physics (from evolution of physics): Physical concepts are free creations of the human mind, and are not, however it may seem, uniquely determined by the external world.
- His love of algebra and geometry was so great that at twelve, he was already confident that nature could be understood as a "mathematical structure".

#### Archimedes
- On love for pure ideas (Plutarch): Archimedes possessed so high a spirit, so profound a soul, and such treasures of scientific knowledge, that though these inventions had now obtained him the renown of more than human sagacity, he yet would not deign to leave behind him any commentary or writing on such subjects; but, repudiating as sordid and ignoble the whole trade of engineering, and every sort of art that lends itself to mere use and profit, he placed his whole affection and ambition in those purer speculations where there can be no reference to the vulgar needs of life.
- On his proof of area of circle equals triangle of height r and base Q (circumference) (Plutarch): No amount of investigation of yours would succeed in attaining the proof, and yet, once seen, you immediately believe you would have discovered it.

#### Others
- On Joseph II of the Holy Roman Empire: "Everything for the people, nothing by the people"

### Talks
#### Alan Kay
- On David Evans: Dave's way was to make something like a garden, and tend that garden so that many things would have many chance to grow by themselves. His idea was to just do good deeds everywhere and every time you can without any hope of return. And much of the time the angelic side of humans will nudge other humans to start helping themselves.

#### Hinton
- On intuition and knowledge distillation: you need to put in a lot of hard work to get sufficient experience in a domain and then you need to trust your intuitions. 
- On politics and science: I grew up in Britain in the 1950's and 60's and a major puzzle at the time was to understand how civilized and well-educated Germans could have allowed Hitler to gain power. Recent events in the US have made that seem a lot less puzzling. ... I believe that highly selected and extremely well-educated students like yourselves have **a moral duty to stand up for the truth in the face of political attempts to suppress it.**

### Movies
#### Oppenheimer
- "When you speak they hear a prophet, when Straus speaks they hear themselves", "They'll listen to the prophet", "The prophet can't be wrong, not once."


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


## Recent Thoughts
- 9.13: reading Dreaming and the brain: from phenomenology to neurophysiology, Building machines that learn and think like people. Consciousness, CNN and k-nn, other inputs coming from working and long term memory to fine tune boundary cases with imagination. Memory of internal thoughts and why are they transient, how are they related to dreams. 
- 9.29: I've successfully connected a brain thought while waking up in middle of night to "note taking" and remembered it once I saw this app