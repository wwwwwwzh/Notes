



# Vision
## Pixel Coordinate
Staring at bright light and close eye. Moving head maintains that light's relative position to eye center in the "big black frontal screen". 

If our perception of space is only from retinotopy of various processing centers, i.e. we know something is left to something else because the actual neuron is to the left of another neuron, each corresponding to their respective real world stimulus. 

The origin of retinotopy is retina. So if the previous theory holds true, a receptor on a certain neuron will only give you one coordinate. However, as shown above simply changing eye direction can alter our sense of where it is in space.

gaze centered->head centered->self centered

## 3D Construction
know the world changes when I move, the change is gradual and slow. -> (depth: move behind it and see what is there + see from front but move parallel to it)systematic observation of object

## Retina


## Movement
### Others
The buildings shown in this image is more easily seen when the picture moves, even scaling works.
![](/images/movement-sensitivity.jpeg)

## Pathway
### Scene Familiarization
It seems that when exploring environments dynamically, both pathways are active. But when statically examining, it's predominantly ventral. But once we get familirized, we concern more about how to deal with objects instead of sensing them.

# Learning
## Building Blocks
### Contrast & Similarity
On a primitive level, contrast exists in all sensual processing. A dark light is perceived differently than a bright light. A sharp pain is different from a slow one. On a higher level, we learned to contrast ideas. For example, we know a circle is different from a square by associating the strait edges with square and the symmetrical curviness with circle. But when we approximate a circle with polygons, it feels natural that a similarity is growing between the two shapes.

### Association

## Things that are there
### Algorithms
Neural circuits are powerful enough to approximate any function and we shouldn't doubt if some function is too complex for biological structures. e.g. pitch differentiation is logarithmic. 

# Memory
## Fundamental Theorem?
1. All memory results from association i.e. adjustment of synaptic strength between neurons
2. Memory strength is a function of time and initial strength. 
3. Each association has its own strength function (doesn't need to naturally decline)
3.5. Association and dissociation are the same

## Memory and Attention

## Dream Memory


## Others
Also see Advanced AI and Brain under ![](/Logs.md)

### Face Similar But Can't Recall
Someone looks familiar but can't remember who he resembles whatsoever until you see that person and suddenly knows that's the one you are looking for. Might be related to unidirection and central theorem two

# Consciousness
### Stop of Noise
At the instant of the stop, you remember/are aware of both the noise before stop and the quietness immediately after. But if no such sudden stop happened, you are neither aware of the noise nor will remember the sound of the noise.

### Consciousness and Memory

## High Level Processing
### Different Ways to "See" Things
https://youtu.be/Si6NbKqYEd8?si=eNuaYrqI1JWTr7hb&t=337

### Why Do We Need Attention or Focus and Much more Energy When We Are Trying to be Precise
e.g. you have a instant thought that sth is true and have a quick thought and seems like you can prove it. but it takes more time and determination to really pin it done. and you can't do this when you're tired


# Major Questions
- Neural circuits that support episodic memory (hopfield?)
- Is perception memory (is memory perception with attention): should perception be regarded as modal specific memory or unconnected memory whereas recall memory stems from either internal or perceptive stimuli and activates connected ideas
- When distant neurons corresponding to originally distant ideas are associated, how does the synapse take short cuts. How does connections outside hippocampus form once hippocampus has done its job.
- Are there really different types of functions of neural circuits? imitation->episodic memory->difference&similarity(pattern)->
Reward vs non reward based learning

## Blueprint
### 10.4
1. The brain can be abstracted as a big network of neurons where each neuron is connected to many other neurons (sparse hopfield where each node is a MLP or transformer)
2. Coactivation of a group of neurons strength the connections of every connections within the group
3. The network is constantly changing while producing output (MLP loop or dynamic hopfield)
4. The first major learning goals are proprioception, visual stimuli as function of time, and interaction between self and the world (discovery of experiment)

# Minor Questions
- Drawing: hand drawing->scribbles->shapes->patterns
- time and place cells in hippocampus. necessary or byproduct
- People say brain learn with few examples. But don't forget how biased we can be: we justify a claim by just one example; we base our judgement for one day on something happening for one minute... In addition, we fail to learn many things with few shots. We can't recognize similar faces at first. We can't easily directly learn a language without grammar background. We have to sometimes infer priors to make sense of observations
- Why concentration and precise language is hard? Does precision require more detail as in visual imagination? I think yes. You first think of something vague, then you its content is used to relate to something more, with more details, then you iteratively add more detail to your description, either visual or linguistic, to obtain something as precise as you want it to be (as away from counter examples)
- Dream, memory, attention, memory of recalling memory, perception vs internal thoughts: when we concentrate on external stimuli, we remember; when we don't concentrate, we don't; when don't remember what we thought about or imagined hours ago; we remember that we did thought or imagined something; we remember trying to recall something either internal or external; we don't really remember dreams without rehearsal; we remember trying to recall a dream. Note that it's easier to remember visual thoughts with "plots" (daydream). However, real dreaming or falling asleep requires giving up voluntary control of the scene and interactions and instead imagine a "static" scene unfold itself.
- Implicit memory is more statistical, it combines large data and get generalizations. Explicit memory is specific and differentiates between details so we can recall things accurately
- Is memory of an emotion reactivating some emotional output or perceptual input to re-elicit that emotion
- high attention in dream seems to lower response to real world perception
- Is RNN equivalent to neuron in terms of temporal and spacial aggregation
- working memory and episodic memory might also be explained as connections within episodes, i.e. between individual detailed features. Thus a hopfield like structure for this kind of memory is likely

# Notes
- look around system: 1. intuitive systems (curiosity, biological needs...) 2. recognize seen objects 3. tell if familiar objects changed 4. tell if objects doesn't conform to mental model 5. physics
- non fixed length attention: each word sequentially generates KVQ. output either start of response or latent (continue to listen)
- sleep spindles actively participate in the consolidation of overnight declarative memory. The density of spindles increase after extensive learning of declarative memory tasks and the degree of increase in stage 2 spindle activity correlates with memory performance.
- cortical and nuclei architechture might be for different purposes (storage vs operation)
- Explicit memory connects specific detail to other specific details that are highly relevant (within the same episode). When it becomes implicit, it can readily be used in thinking and talking without being activated by those specific details.
- dream memory is sometimes real memory but mostly "fake"