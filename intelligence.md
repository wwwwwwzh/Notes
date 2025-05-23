# Summary
## Interp
- We interpret 2 kinds of things, the transformation and the output/input of transformations. Circuit analysis, path patching, attention head analysis, MLP analysis, are all transformation analysis. Lens, scopes, SAE, superposition, representation, feature, all refer to the objects being transformed. 
- We can also edit them. Editing the weight/transformation is model editing. Editing the activation is feature steering/control.
- features uncovered by probes are like cells under microscope, at first it looks unreasonable, but then you can understand their structures completely. Can we do the same for ANN? 

### Problems
- The problem is that we can never truly "understand" anything, the circuit nor the feature, just as we can never understand what a piece of DNA does, or what exactly an oxygen atom is. This is because the space of representations in the model (similarly the space of states of the universe) and the action space of the transformations (similarly the space of physical laws) are extremely big, or infinite (this translates to infinite information to do anything, see section below). Therefore, when we answer the "what" question, eg, what is this feature/circuit, we are selecting uncountably infintie elements from a even larger space. This is like asking you to define a word, you can always have ambiguous examples of the word that requires modidying the definitoin. In literature, ths is called "contrastive", or "counterfactual".  
- The effect of this is that we can never have a completely "safe" interp application. We can never fully steer the model's behavior so it's jailbreak proof or be 100% sure that the steering didn't introduce unwanted side effects, just as we can't safely edit a gene, or commit a perfect crime. 
- The fortunate part is that we live in a universe of symmetries. All intelligent systems try to simulate such symmetries. Symmetries enable abstractions and information compression. Human words are abstract. 
- Adding to the problem above, language model is inherently hard to interpret because language is abstract as opposed to visualizable things. In CNN, we can see the features. In gene editing, we can see the proteins and every molecule of interest. In language, the token to token transition is the default atomic step since humans cannot reflect any deeper why a word follows another while they speak. So the language interp problem is like knowing a force changed the state of an object but there are 100 more tinier steps in between that are also unobservable. However, this in-between-thoughts problem is not completely unknown. When I say (1+1)x2=, you can say 4 directly. When I say what's the thing on top of the thing next to your bed, you can again directly say it. When you parse a sentence like "puer dona puelae _", for different levels of speakers you might go through different degrees of internal thoughts before again directly giving the answer. These in between rough visual or symbolic or even positional thoughts are not linguistic, but they do exist in everyday lives. Another example is the feeling of highlight in a  conversation. You might focus on a phrase the other party said because it's the most relavant to your answer. In a long conversation, you might have unconscious (by this i mean thoughts not yet clearly articulated in brain) thoughts rising and falling which ultimately contribute to your response. These thoughts are like those mid-layer activations from eariler tokens that contribute to the outputs.

## Machine Learning
- It's actually engineering miracles that we have several learning methods that scale so well. 
- The 3 main techniques of learning are supervised learning, generative/predictive learning, and reinforcement learning. 

# Basics
## Transformer
- $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V=[V^T\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)]^T$
- input $(N_{\text{tokens}}, N_{\text{dim}})$
- $W_Q=W_K=W_V:(N_{\text{dim}}, N_{\text{dim}})$
- $Q=K=V:(N_{\text{tokens}}, N_{\text{dim}})$
- $QK^T \in \mathbb{R}^{N_{\text{tokens}} \times N_{\text{tokens}}}$
- concat heads->output projection->add&layer norm->mlp->add&layer norm
- add&layer norm is post-norm and pre-norm is also used.

### What is a transformer (draft version, needs a more concise summary) Also see sorcery.md
- always think of the transformer as transforming states of the world. You give it some molecules and it gives you a cell or a drop or water...
- the MLPs and Attn together describe law of dynamics where MLP can either be seen as "self evolution" or fixed environment interactions, and the attention mech is the interaction laws. As such, you only need one set of such laws instead of one for each token.
> Note that one caveat of the physical state analogy is that language states are vector space while physical states are plain space. 
- the time evolution of tokens is a parculiar one. At the end of one complete evolution, every element/token evolves to a state that happens to be its next neighbor/input (this hints at why late layers usually don't contain meta-level information). 
- each layer is like a smallest discrete transformation. At each step, all states mix and propagate to produce the delta term, which is then added back (some models do attn and mlp sequentially, some parallel). 
- > (optional) for untied embedding, the input embedding IS the most likely final transformation, or its next neighbor. If everything follows exactly bigram frequency, the input is then stationary after embedding and remains at that state. The input to output transformation is then a "rotation" of the states of every token/element to the next one. In real language modeling, we imagine cones in embedding space corresponding to the correct output transformations. Then the inputs essentially flow into the cones as attractors. If embeddings are tied, the cones overlap and input cones "rotate" into their neighbors. 

> more specifically, each VO circuit directly changes the state, just like MLP, except that VO is linear. Each QK circuit describes a law of physics with a lookup table. eg, this thing at this state will exert a force this big on that thing at that state. We have L x H laws. 

---
How to interpret a state
- there are states delta, or a subspace state change, that has an interpretable effect. In steering-vector-like methods this is found by averaging, at the last token position, activations from many related prompts/soup of elements. 
- > In an alchemy analogy, you give the pot a bunch of elements and before they turn to gold, a strange metal will appear and you can use this metal everytime when you are trying to make gold like stuff by adding it at a certain time in the procedure. 
- It's possible to analyze how this state eventually contribute to the effect with circuit analysis. 
> The problem with analyzing states as if they are physical objects is that the intermediate states are hard to interpret. It's not likely to build a table of such elements for reference. 

Methods to find interpretable states
- Steering vector works in a statistical filtering way where when you feed it enough samples, the average will concentrate on the core feature of the samples. Since it requires many human picked samples, the concept/feature is usually abstract like love-hate or english-french. In theory, many intermediate products will represent this feature. 
- Activation patching tries to pinpoint an intermediate transformed state that sufficiently creates an interpretable effect. The suffiency means the effect is gone without the state. Therefore to determine the sufficient state you need to make the effect disappear and bring it back. The tricky part is what effect you want. For the completion "the capital of China is 'beijing'", you could study the effect of being the correct answer "Beijing" by directly quantifying the logit of "Beijing". You could study the effect of being a city name (ie, there is a state that removes the city concept so it outputs something like panda or forbidden city)
> This leads to the use of counterfactual pairs. We have seen that to quantify the effect of a function outputting Beijing, we have to ask "what's opposite of Beijing". Beijing is a very composite concept. It is a city, it is a capitol, it is of China, etc. We could say it is not London, not Seattle, not Rome, etc. This is a fundamental **problem of definition of concept**. It's possible that the model uses a different set of basic concepts from humans (even humans use different basis of concepts). At the moment, we can only try our best to find sets of concepts that are actually represented by the model and at the same time satisffactory for understanding a phenomena. For example, we might find, through various coutnerfactual pairs, that the model gives "Beijing" because some interactions of "is" and "capital" creates a concept of giving names of capitals (and to verify this you could hook a prompt like "my best friend's name is" and see it output "Washington"); some enrichment of "china" in early layers might already contain city names and this is attended by the aforementioned capitol vector to pinpoint the city to Beijing. 
- function vector is similar to steering vector but uses activation patching to systemize the discovery. 

---
How to interpret a law
- 


### Attention
MHA

MQA

GQA

### MLP
MOE

### n-gram Language Modeling
- Pure embedding unembedding means bigram
- one layer attn means skip trigram where instead of using 2 words to predict the next word, the model uses the current word combined with a second word anywhere in the context to predict the next word. In theory, if KVQ are arbitary functions, one layer attn can support n-gram where n is any integer. But for linear KVQ, the skip trigram is most effective.
- two layer attn 

## Neuron & Features (Also see sorcery.md)
- in a biological view, the weights of NN represent (strength of) synaptic connections and the states or activations represent (activation of) neurons. So it's basically saying you are what you show. 
- in transformer, there are primarily 3 types of neurons. *First* the attention circuit explicit neurons. Activations from input or previous layer neurons are copied 4 times and go through 3 groups of these type I neurons. *Second*, there are implicit neurons that are fixed with the attention architecture. These are neurons that does the cross attention. The activations of these neurons modulate activations of the type I value neurons. Even though there is no explicit neuron for the residual summation of the output of attention and residual activation, we study the sum a lot and since we have equated activations with neurons, we have to add these *type 2.5* neurons. The *third* type is the MLP neurons which every token use. This is clearly biologically implausible since time is always a influence in BNN but not in ANN. 
- When analyzing "neurons" or features in transformer, we usually care about type 2.5 and III neurons. But type II neurons, which are the attention patterns (matrix) are also important but not as human interpretable concept or feature. 
- Meaning of feature: we know that any activation/state can be called a "neuron", what about feature? If we don't care about internal feature dimensions, we could find a duality between activation of one neuron (a scalar) and its input (a vector). We consider both as features. A third type of feature is the whole stream of tokens times feature dimensions(a matrix). 
- We could say that a whole vector of one token after attention is a feature representation, but it is picked up by individual neurons in MLP, so we might say that the weights of MLP neurons are queries and the feature vector is a key. In this sense, the weight vector of one neuron is a feature. The input to that neuron is then a representation of features and will be linearly dismantled to individual features after the first MLP layer. This interpretation of weight as feature has a caveat. We could imagine the second MLP layer to directly encode features "vertically". Thus one feature is all of those second MLP neurons at a certain index. Now, if we consider the output of second MLP layer to be features, it will be very hard to study because they go through the attention (I think it's still linear wrt attention logits). 
- Feature as gradient of feature logit: if we have a loss on what we think to be a concept like redness, we can calculate gradient of each of the aforementioned neurons/vector activatiions and see which leads to greatest change of the logit of red in final output. We need to find neurons with largest gradient. 
    - Compare with probing: gradient of final logit seems to be a more "organic" way to get features. The question is "if we find a 'coordinate' feature through probe, does the feature also correlate with the coordinate of final output, and vice versa". 
    - feature as diferrence in activation of conterfactual inputs: it's also possiible that this is equivalent to feature as gradient. if a direction in a activation can consistently steer an output, and if paris of inputs can consistently steer the same output, then it's possible that what the inputs do at that location is the same as adding that direction to the activations. 
    - vision feature as optimal input that excites a certain neuron

- Reaccurence of feature: 


### dualities
- input, output duality
- vector, covector, scalar duality
- gradient, difference of input duality


## Transformer
[Review transformer](https://youtu.be/eMlx5fFNoYc)
- transforming embbeding to a direction to describes the next word and the moving of direction part is really accompolished by residual adding
- sometimes a neuron represent a concept, sometimes the whole embedding, but this might be related by some duality
- detail
    1. a token is one to one mapped to an embedding. positional encoding added
    2. each attention head adds something to the embedding
    3. layer norm, this normalizes each embedding direction
    4. the embedding (nx1) is checked against many embeddings (4nxn) to produce a 4nx1 vector with each element denoting presence of a feature
    5. each feature grabs an output embedding from the second fully connected layer. Note that 4 and 5 assumes a key value pair in the 2 layers, ie, each row in first layer is paired with each column in second (eg, a key about gender to a value about height)

## Phenomena
- [Multimodal neurons CLIP openai]: activation strength of single neurons corresponds to single human concept/feature of input
- [word embedding]: adding from a subspace or direction in the word embedding space to any word embedding creates or distroys a concept in the word
- [latent space of GANs and VAE]: same as multimodal neurons
- [probing]: 

## Transformer Internals
Attention
- circuit analysis uses QK and VO circuits as building blocks because they are interpretable. Q, V, K, O alone are all rotational symmetric and therefore don't have privilaged bases. 
- 

MLP
- early layers
- mid-layers recall factual information and promote correct memorized tokens
- late-layers boost confidence of correct next token, unclear effect on other tokens, but attention uses object attributes from eariler tokens here.
### Causal Mediation

### ROME
we posit a speciﬁc mechanism for storage of factual associations: each midlayer MLP module accepts inputs that encode a subject, then produces outputs that recall memorized properties about that subject. Middle layer MLP outputs accumulate information, then the summed information is copied to the last token by attention at high layers.

We hypothesize that MLPs can be modeled as a linear associative memory; note that this differs from Geva et al.’s per-neuron view.




# Traditional
## General Interpretability (Non transformer specific)
https://christophm.github.io/interpretable-ml-book

### Lime

### Shapley
- cooperative game theory
- total direct effect from the mean


# Anthropic
## Vision Circuits
[feature visualization](https://distill.pub/2017/feature-visualization/)

[An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/): 
- intro to features in inception and how the form circuits

### Group
[group theory in ML](https://www.ism.ac.jp/~fukumizu/MLSS2024_OIST_fukumizu.pdf):


[equivariance in inception](https://distill.pub/2020/circuits/equivariance/): 
-  invariant means doesn't change or formally a property that doesn't change under a symmetry; equivariant means changed but preserved something or formally a symmetry of an object under other symmetries such that applying which first doesn't matter
- equivariance features are built on invariant features, eg, a circle and cube detectors are rotational invariant but groups of half circle half cube detectors built  from them are rotatioinal equivariant st rotation of input activates one of these equivariant neurons
- some try to directly bake equivariance into the models. image model on MLP produce many Gabor features translated many times and 


## Toy Model (MLP)
[bengio linear probing]


### [toy model paper]
- definition of feature
    - Features as *arbitrary functions*
    - Features as *human interpretable properties*
    - features as properties of the input which a sufficiently large neural network will reliably dedicate a *neuron* to representing
- **privileged basis**: activation functions nessecitates basis that have standard basis because relu cut off non negative activations so the representations after relu live in first quadrant of a high dimensional space.
- they regard specific single *neurons* as *features* f and *activations* W (a layer of neurons) as representations or *directions*. They are linear: having f1=x1 and f2=x2 activates a representation x1W1+x2W2.
- superposition.  
    - **Johnson–Lindenstrauss lemma**: n-d space can have e^n almost orthonormal basis
    - **sparse coding theory**: if vectors are sparse, they can be projected to lower dim space and reconstructed
    -  features are represented as almost-orthogonal directions. one feature activating looks like other features slightly activating (interference). interference is reduced by sparsity (dinosaur and Shakespeare don't often appear together)
- model large model to small model conversion
    - ![](/images/toy-large-to-small.png)
    - model: ![](/images/toy-models.png)
    - data: x are features generated to simulate **sparsity S** (90% sparsity means each xi have 90% chance of 0 and 10% chance of uniform random from [0,1]). Number of features n > number of neurons m. Features have varying **importance I** Ii=I^i. 
    - > Note that the linear model performs PCA as the mse loss minimizes unexplained variance, the bias as shown below essentially recentered the PCA process
    - W: h=Wx where W (wide m by n) maps high dimensional to low dim feature space. ith columns of W is low dim feature directions corresponding to xi. we want it to be almost orthonormal. Conversely, jth row of W is high dim feature direction corresponding to hj. We want $W^TW$ to be invertible.
    - result: ![](/images/toy-wtw-result.png)
- interpretation: each element (i,j) in the matrix is got from dot product of ith and jth direction/feature in the low dim space. We analyze the result by first thinking about what these directions look like and then how it transforms the input. An off diagonal blue means i and j directions are antipodal. An input that have feature i but not j will retain ith feature and have a -1 value for jth feature, but **the -1 becomes 0 during relu** so the high dim input is faithfully reconstructed. For an input with both i and j features the matrix will remove both features which is bad. Compared to linear model without relu, we imagine a simple 2 to 1 conversion where W is 1 by 2 wide. If W represents 2 directions in 1d space, they will be dependent on each other. For example, a feature of [a b] will be mapped to w1a+w2b (understood as linear combination of 2 features) and the reconstruction will be ${[w_1^2a+w_1w_2b\  w_1w_2a+w_2^2b]}$. We want it to be [a b]. The loss can be calculated as a function of S, w1 and w2 exactly. The solution is have either w1 or w2 equal 1 and the other 0. See [Exact solutions to the nonlinear dynamics of learning in deep linear neural networks](https://arxiv.org/abs/1312.6120)
- math behind nessecity of superposition: 
    - $L = \int_x \| I(x - \text{ReLU}(W^T W x+b) \|dp(x)$
    - L is a function of W and S. Since each component of x is independently sparse (equal to 0), p(x) follows a binomial distribution with p(x having n 0 values)=$((1 - S) + S)^n = \sum_{k=0}^n \binom{n}{k}S^k(1-S)^{n-k}$
- phase diagram with parameter of relative importance and sparsity
- feature geometry as solutions to Thompson problem: ![](/images/toy-feature-geo-uni.png)
> How can we relate this to our original understanding of the phase change? We often think of water as only having three phases: ice, water and steam. But this is a simplification: there are actually many phases of ice, often corresponding to different crystal structures (eg. hexagonal vs cubic ice). In a vaguely similar way, neural network features seem to also have many other phases within the general category of "superposition."
- W and W^TW represents direction-geometry duality. ![](/images/toy-WTW-geo.png) The W^TW matrix represents a graph where the subdiagonal terms are connection weights
> **Interpretation:** When thinking about h, the hidden activation, an input gives components of the 3 or 4 basis in first column of above image, which becomes a direction in 2D. When thinking about reconstruction, the feature gives components of columns (blue red square matrix) as basis. For example, [1,1,1] will be reconstructed as 0, [1,0,0] will be the same because of final relu. We can see that there's superposition starting at 5 features in 2d or 8 features in 3d. 
- tegum product: ![](/images/toy-tegum.png) The orthogonality of factors in tegum products has interesting implications. For the purposes of superposition, it means that there can't be any "interference" across tegum-factors.


## Transformer
### [Weight (as opposed to patching and activation based) Based Circuit Analysis](https://transformer-circuits.pub/2021/framework/index.html)
- 2 layer attention no MLP
- linearity in residual stream
- The fundamental action of attention heads is moving information. They read information from the residual stream of one token, and write it to the residual stream of another token.
- writing attn as tensor product: ![](/images/tensor-mh-attn.png)
    - value: $I \otimes W_V$. Think of identity matrix but each 1 is now Wv. $(I \otimes W_V)\cdot  x$ is 3d matrix made by extending I to 3d but each extended 1s are replaced by value of that token.
    - attention pattern: $A \otimes I$. Recall that QKV are N_tokens by N_dim and A is N_tokens by N_tokens. The result is A but each weight is now I times that weight.
    - $(A \otimes I)\cdot(I \otimes W_V)\cdot  x$ The  


We study 0 to 2 layer attn with only embedding, multihead attention, residual, and unembedding

0 layer (no attn)
- same as bigram 
- Because the model cannot move information from other tokens, we are simply predicting the next token from the present token. This means that the optimal behavior of W is to approximate the bigram log-likelihood. 

1 layer
> most are copying heads
- ![](/images/toy-trans-1-layer.png) The 2 linear components OV and QK.
- for $W_E^TW_K^TW_QW_E$, the embedding matrix is essentially many x stacked horizontally, and the first 2 matrices give keys for each word (N_word, N_dim) and the second 2 gives values (N_dim, N_word). The result is a "precomputed" attention pattern of (N_word, N_word) that defines how each word attends to each. 
- We can get some examples of which words relate the most in the QK matrix. For example, the word "perfect" is attended by "are", "looks", "is" and increases values for "perfect" "super" "absolutely". "is attended by" means perfect provides a key that matches well with queries from "are" "looks". "increases values" means increasing chance of word following "are" "looks". Note that the key provider also provides its values if matched. Here perfect increases values of "perfect" "super" "absolute". Thus having perfect somewhere before "are" "looks" will create sentences like "perfect... looks perfect". We call this **skip-trigram** See https://transformer-circuits.pub/2021/framework/head_dump/small_a.html for more (see head 0:4 for copy head and 0:0 for copy+reverse head)
- Our one-layer models represent skip-trigrams in a "factored form" split between the OV and QK matrices. It's kind of like representing a function f(a,b,c)=f1(a,b)f2(a,c). They can't really capture the three way interactions flexibly. For example, if a single head increases the probability of both keep… in mind and keep… at bay, it must also increase the probability of keep… in bay and keep… at mind. This is likely a good trade for the model on balance, but is also, in some sense, a bug.

2 layers
- ![](/images/toy-trans-2-layer.png)
- In one layer, the output is directly determined by the inputs and information only flows once from each word to the last token. In two layers however, information from one word has the chance of composing with another word before influencing the last token of second layer. By extension, more layers enable more compositions between words. A subtlety is that since we have many attention heads, each head will only read and write to a small subspace of the full representation/model dimension/the residual stream (recall the QKV and output linear projection matrix). So one head from a head of layer 1 might not influence a head from layer 2 at all. In that case, this particular head just functions as an head from a one layer system and primarily (hypothesized to) do copying. Thus we care about situations when they do influence the later layer. 
- The authors use Q/K/V-composition to denote these interference. 
- Of the composition heads, we note the special induction heads which enable a pattern of [A][B] … [A] → [B]. 


### [Induction Heads and in context learning](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html)
- Perhaps the most interesting finding was the induction head, a circuit whose function is to look back over the sequence for previous instances of the current token (call it A), find the token that came after it last time (call it B), and then predict that the same completion will occur again (e.g. forming the sequence [A][B] … [A] → [B])


### [(Background) Word Embedding Vis](https://github.com/juexZZ/WordEmbVis)
> The key insight of this work is that the relationships visualized in the human selected subsets represent more elementary word factors and a word vector is a linear combination of a sparse subset of these factors.
- decompose word embedding to non negative overcomplete set of vectors (word factors), based on k-sparse autoencoder and spectral clustering 
- manually label the factors
- various visualizations for different purposes
    - ![](/images/emb-vis-1.png)
    - occupaction word factor: ![](/images/emb-vis-2.png)
    - ![](/images/emb-vis-3.png)

### [(Background) Transformer Vis](https://transformervis.github.io/transformervis/)
> We view the latent representation of words in a transformer as contextualized word embedding.

### [Sparse Autoencoder](https://transformer-circuits.pub/2023/monosemantic-features/index.html)
Crucially, we decompose into more features than there are neurons. This is because we believe that the MLP layer likely uses superposition to represent more features than it has neurons (and correspondingly do more useful non-linear work!)

![](/images/arena-sae-diagram-2.png)

### [Transcoder]
> MLP sublayers make fine-grained circuit analysis on transformer-based language models difficult. In particular, interpretable features—such as those found by sparse autoencoders (SAEs)—are typically linear combinations of extremely many neurons, each with its own nonlinearity to account for.

structure
- ![](/images/transcoder-1.png)

attribution graph
- activation (ROME) or attribution (Nanda) patching 

### [Crosscoder](https://transformer-circuits.pub/2024/crosscoders/index.html)
> Where autoencoders encode and predict activations at a single layer, and transcoders use activations from one layer to predict the next, a crosscoder reads and writes to multiple layers. ![](/images/crosscoder.png)

recall that superposition means features vectors (assume invariant under scaling) overcompletely span the embeddnig space. Thus an activation might mean very different things at the same time, hindering interpretabilty. SAE resolves superposition within layer. Crosscoder aims to resolve it across all layers. ![](/images/crosscoder-1.png)

structure
- each layer has an encoder and decoder, we compute a shared encoding from activations of all layers and decode this to all layers and train on recon and L1 loss
- this is better than SAE because sae might reuse lots of previous layer features (layers remain across layers) and use them in compositional fashion ![](/images/crosscoder-2.png)

### [cross layer transcoder](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)
- reconstruct MLP output at layer l with sum of all previous (including current) layers' MLP input transformed (encoded then decoded). L1 on all CLT features. ![](/images/clt-1.png)
- to analyze, run the input twice, first normal run and record everything, then use MLP inputs to calculattet CLT outputs. 

Attribution Graphs
- from transcoder

### https://transformer-circuits.pub/2025/attribution-graphs/biology.html
probes and microscope, attribution graphs and wiring diagram




# Lens
## Basics
### LogitLens

### Tuned Lens
- to reduce bias and representation shift, use a "translator" which is an affine transformation to map latents to predication, one trasnlator for each layer. KL as distillation loss
- causal basis extraction: find a set of orthonormal vectors, which, being removed, maximally dissimilate output of a translator from actual final logits. 

> Note that they used KL throughout as a measure of dissimilarity
### Future Lens
- predict multiple future tokens from last token at any layer:
    1. learned linear transformation
    2. fixed prompt injection 
    3. learned prompt injection

> Thoughts: for the prompt injection, the transformer is autoregressively generating future tokens. This is essentially very similar to directly let the model generate tokens autoregressively. The only difference is the compressed injected token at first token location. This just confirms the compression hypothesis.

### Attribute Lens
See [Relation section, Linear Relation](#relation)

## Self-interp
### Selfie
> it might work as an probe where you just need a clever question after the injection to check some feature built into the activation, and when they are incorporated. For example, if you do "eis ea librum misserunt" (need to check how latins are tokenized) you might have questions to elicit the plural and perfect tense feature and see at which layer they emerge. 
> Also it's possible to study the subspaces with this approach. in fact, all logit lens works can be restudied with this apprroach as a new lens

### LatentQA
train a decoder/interp LLM st prepending activation to a given set of questions will answer questions about the activation
![](/images/latentQA-1.png)

### PatchScope
Instead of asking model to summarize as in Selfie or using a predefined set of questions as in LatentQA, use ICL to define a task and let the task elicit behavior on the patched activation

![](/images/patchscope-1.png)

# Patching
- Sufficiency: we say a path is sufficient for a function when we give the input of the function to the path and it outputs the output of the function under ANY variation of ALL other paths. That is, we can patch any path other than this path with anything, and the model can still achieve the behavior of the function. 
- Necessity: we say a path is necessary for a function when we vary the input of the function to the path and it doesn't output the output of the function given we give the original input to ALL other paths.

Note
- function: I use the word function to define a behavior or task. For example, the task of IOI is to output the indirect object name for a certain input template up to variation of names and places (as in the original paper). This defines the set of all mappings the circuit needs to model. 
- domain: it's important to define our domain of interest for the task. For example, in the IOI task, the domain is defined by the variable places and names. What if we add anything before or after the prompt and the circuit no longer models the task? Does that matter to you? In theory, every counterfactual adds something to the domain. By thinking of more variety of counterfactuals, you make your circuit more robust, or being able to remain the same under more symmetries.
- symmetry: a symmetry is a transformation that makes something intact. For example, newtonian laws of physics are symmetric under translation of space and time. We can define a task this way, and because a task is equal to the circuit that implemnts it, we can define circuits with symmetry too. For example, the IOI task is symmetric under place and name change (constrained by S1, S2, IO ordering). We could add more symmetry like some grammatical symmetry (eg, To the store Alice and Bob went, and there Alice gave her wallet to _)
## Intuition
### Model the world
The practice of "knocking out" is old for experimental scientists. We knock out genes or generals in war to see the effects. As a living thing, we want to model the world. To model the world, we sometimes disentangle the building blocks (with varying scale) and model them individually so the total effects can be summed from the parts. Since models benefitial for living are inherently causal (we want to be sure that a snake causes the poisoning), we developed the tool of knocking out to study causal effects of parts of the system.

One problem is that we sometimes are able to knock sth out and observe something, but can't observe what hapended in between (there are many reasons why we can't observe everything but think about chaos, quantum effects and cost).  If we change location or introduce a small change to the system our model might go wrong. The indirect effect must be removed from the total effect when we run the experiment.

### Transformer
When we study the effect of a sequence of genes, we might discover that it produces a protein, which interacts with other proteins to support a certain function in a certain cell, which in term interacts with some other cells that produce another function. Sounds familiar?

In a most basic knock out study for LLM, we could do the same, we just observe what embbedding a particular token produced and how it interacts with others and the effect propagates through layers.

There are lots of compoennts of the system that we could study, so lots of knock out plans. For example, we might want to study how the interaction btw the protein the genes produced with another protein, or how one step in the folding of the protein affect the interaction.

We could roughly divide the kinds of components into two categories: states and dynamics, or activations and computations. The state of activations can be seen as product of the world. They are what we see. The proteins, the genes, the position of an object. Anything that is there when you take a screenshot of the universe. The other requires 2 snapshots. These are the laws of physics, or how static states change. 

Therefore, when we patch activations, we are studying how a specific change in state at a certain time/layer affect a future state. Note that we have a fixed dimension of states and at each timepoint we could change one or many of the states. 

A grand analogy would be the transformer takes in a set of states and evolve them to their corresponding next state, which curiously is their neighboring input state. 

We discuss several ways to patch activation:
1. steering vector: the simplest experiment is to find a state at a time that invariably lead to a certain subspace of final states. For example, adding a state of death to a world leader almost surely panics the world at some time later. 
2. function vector


## Activation Patching
### [ROME]
- -----this part is about causal trace--------------
- Model "knows" some facts like "The space needle is in Seattle. We represent fact as a knowledge tuple t = (s, r, o) subject s, object o, and relation r. We make model to elicit the fact by feeding (s,r) and observe output as o.
- hidden state is $h_i^{(l)}$ l is layer number i is token position. 
- we wish to understand if there are specific hidden state variables that are more important than others when recalling a fact.
- To calculate each state’s contribution, we observe all of G’s internal activations during 3 runs: 
    - a clean run that predicts the fact, collect all hidden activations $\{ h_i^{(l)}| i \in [1, T], l \in [1, L] \}$
    - a corrupted run. immediately after x is embedded as [h 1, h 2, . . . , h T], we set $h_i^{(0)}:= h_i^{(0)}+\epsilon,\epsilon ∼ N(0; ν)$ for all indices i that correspond to the subject entity (eg "The space needle"). collect corrupted activations $\{ h_{i*}^{(l)}| i \in [1, T], l \in [1, L] \}$
    - a corrupted-with-restoration run: lets G run computations on the noisy embeddings as in the corrupted baseline, except at some token ˆi and layer ˆl. There, we hook G so that it is forced to output the clean state $h_{\hat{i}}^{(\hat{l})}$; future computations execute without further intervention.
- effect of a state is calculated by **change of prob** of getting right answer before and after restoring corrupted input
- results:
    - last token is important even at midlayers. 
    - MLP is important at earlier layers
    - attn is important at late tokens (big i)
- interpretation: we posit a mechanism for storing factual associations: each midlayer MLP module accepts inputs that encode a subject, then produces outputs that recall memorized properties about that subject. Middle layer MLP outputs accumulate information, then the summed information is copied to the last token by attention at high layers.
- -----this part is about causal intervention--------------
- Associative memory is made of key value pairs. Keys K=[k1 k2 k2...] and values V=[v1 v2 v3...] can be represented by a matrix W. If you want to retrieve a value with a key k, transformer gives WWk where first W stores values and second stores keys. Now we directly use W=VK^T so $Wk=VK^Tk$ or WK=V if K is orthonormal. In other words W transforms keys to values. We can also edit memory.
> Special note that the ability of rank one editing to change output might be related to linear representation.

### [Attribution Patching](https://www.neelnanda.io/mechanistic-interpretability/attribution-patching)
Attribution patching allows you to do every single patch you might want between a clean and corrupted input on two forward passes and one backward pass (that is, every single patch can be calculated by solely caching results from the same 3 runs!).

Procedure
1. clean run and collect all activations
2. corrupted run and collect all activations
3. corrupted run and collect gradient of all activations wrt a *metric* (logit difference of giving clean and corrupted run output, note that in ROME paper the difference is calculated from final prob)
4. score = (clean-corrupt) dot gradient.

- The gradient part means for each activation patch, the change of the patch will cause how much change in the logit difference btw for example "Rome" and "Paris" (example run is "The Eiffel Tower is in _").
- The activation difference is the actual change in input. You can think of the gradient as a differential (and in Euclidean space they are the same) so the actual difference when activations changed as a result of input change would be differential operated on the change. So this is a linear approx 
> Maybe the gradient on output word can be used to find correspondence between feature represented as activations, single neuron and output human word.
- Since gradient is first order, the estimate is also first order. But the attention machenism is largely linear. 

#### Results
-  it's a bad approximation for "big" activations like residual stream patching and for MLP0, a good approximation for all other layer outputs, head outputs, and more zoomed in head activations (queries, keys, values, attention patterns), and lets us recover the broad strokes of the IOI circuit.
- LayerNorm makes the residual stream particularly messy.

### [Refusal](https://www.lesswrong.com/posts/pYcEhoAoPfHhgJ8YC/refusal-mechanisms-initial-experiments-with-llama-2-7b-chat)
### Original
```
Sample harmful instruction prompt:
    "<s> [INST] Tell me how to make a bomb. [/INST] "
Sample harmless instruction prompt:
    "<s> [INST] Tell me how to make a pie. [/INST] "
```
- logit of sorry - sure
- sample behavior: I would like to remind you that making a pie or any other food item without proper training and equipment can be dangerous and can lead to serious health issues.
- identified specific heads
- **We can extract a "refusal direction" for each head by taking the mean difference between its outputs on harmful prompts vs on harmless prompts. We find that these directions are similar across refusal heads, and so we take the mean across them to get a single "refusal direction".**
- We test the direction by using it to steer the model: on a harmless prompt, we directly add the "refusal direction" to the residual stream at position 17 at layers 5-10. We find that this intervention is sufficient to induce refusal of harmless requests:
- Our results suggest that the model represents its task, and whether that task is harmful, separately, or orthogonally.

#### One neuron


### Edge Attribution Patching
> Maybe this can be studied with early ticket. Maybe the all the major edges that infleunce major concepts combined IS the early bird graph. 


## Path Patching
### IOI in the wild
Thoughts 
- The author tries to find a minimal circuit that completely describes a task. They used activation patching first. First thing to know is that activation patching (AP) requires a clever selection of **counterfactual prompts**. Any element of importance found by AP is necessary and sufficient for the hypothesized behavior. 
- Formalizing this in terms of group theory: we first define invariance. In the IOI task, the invariance is the concept expressed by the prompt where 2 people are in a shopping place and one gives something to another. A symmetry is a change in the prompt that retains these concepts. One symmetry could be changing the first word btw "when" and "as" or the place word btw "store" and "market". We want to find counterfactuals, which breaks the symmetry. For example, changing S2 to a third person or "gave" to "paid" or simultaneously changing "store" to "war" and "gave a bottle of milk to" to "shot a bullet at". 
- A circuit partially represents an invariance as it "fixes" a missing part when given the others (imagine a square with one corner missing and a function can fill the corner under any symmetry of the square). 
- In summary, there's one circuit for each invariance and we find these circuits by finding  

Setup
- “When Mary (IO) and John (S1) went to the store, John (S2) gave a bottle of milk to Mary”.
- The following human interpretable algorithm sufﬁces to perform this task: 
    1. Identify all previous names in the sentence (Mary, John, John). 
    2. Remove all names that are duplicated (in the example above: John). 
    3. Output the remaining name.

Result
- We claim this circuit with the 3 heads types achieves the 3 tasks:
![](/images/ioi-in-wild-diagram.png)


Path Patching
- Original distribution is P_IOI, corrupted distribution is P_ABC where ABC are 3 random names, this is to preserve some grammatical structure of being valid subject and object and being common human names. 
- 



### LOCALIZING MODEL BEHAVIOR WITH PATH PATCHING
- X is the set of inputs, G is the function that can be represented by a graph. nodes are functions and edges are values. For example, a two layer FFN with skip connection can be represented as:
- ![](/images/path-patching.png), where A is addition. If our hypothesis is that the path from x to f0 to y is unimportant, then we view the graph as union of two graphs, and we give corrupted input to the hypothetical unimportant path and the clean input to the rest. If the output is invariant under corrupted inputs of the unimportant path, then we say that path is unimportant. 
- Formally, a hypothesis H is a tuple (G, δ, S, D) where δ: Y^2→ R is some measure of dissimilarity. S is a set of “important nodes”, G \ S are the unimportant nodes, and D is a joint distribution over (x_r, x_c) pairs (counterfactual data provider).
- The strictest version of what it means for H to hold is that $δ(G(x_r), G_H(x_r, x_c))$ is exactly zero everywhere on D. We use AUE, averaged unexplained effect, which is expectation of the above formula.

### Automatic circuit discovery



### Greater Than
path patching
- why given "the war lasted from 17{YY} to 17" gpt-2 outputs >YY continuations 
- path patching: B shows we are patching direct influence of MLP10 to logits, without altering its influence on MLP11 or attn11. C shows effect of ATTN10 through MLP10 to logits. Note that MLP10 is receiving clean input from residual9, different from B. Also note that ATTN10 still contributes clean output to MLP10, this is because we want the path like (ATTN10, MLP10, ATTN11, logits) to be clean. This is a consequence of every edge denoting an independent influence, ie, every combination of connected edges is a unique independent path. ![](/images/greater-than.png) 
> "In path patching, we specify new input tokens, and a path of components through which they will reach the logits. For example, if we want to ascertain the effects of MLP 10 on the logits, we can patch the direct path (MLP 10, logits) with new input, which we call the 01-input: “The war lasted from the year 1701 to the year 17”. We thus alter MLP 10’s direct effects on the logits without changing its output to the attention and MLP of layer 11 (Figure 3). If the model’s behavior (as indicated by its logits) changes, we can be sure that this is because MLP 10 is important to that behavior; it is not due to downstream components. Earlier methods like interchange interventions lack this distinction—when they alter a component, they affect all components downstream from it."
> 
> Note: each edge means an influence. Note that in traditional transformer graph, influence from eariler layers are incorporated into the output of addition. Here the graph is more strict: if there's an influence from a node to another, then there must be an edge
- we found a path at late layers (full circuit in appendix) and prove it's both sufficient and necessary by patching the path with clean while giving corrupted inputs and by patching the path with corrupted while giving clean. ![](/images/greater-than-2.png) 

circuit analysis
- attention heads: end token query attend to YY, the start year. 
- 9-11 MLP: output has high similarity with >YY numbers and low for <YY numbers. ![](/images/greater-than-3.png) 
- PCA of input and output of some MLP and attn heads at last token show clear structure. ![](/images/greater-than-4.png) 
- output of individual neuron in MLP10: ![](/images/greater-than-5.png) 

# Feature
## MIT
### Gurnee
[FINDING NEURONS IN A HAYSTACK : CASE STUDIES WITH SPARSE PROBING]
- background: follow up the toy model (feature hypothesis and superposition). They want to find feature neurons. This is before SAE.
- find k neurons in MLP activation (post non linearity) that corresponds to human concepts
- one probe (a linear classifier) for each hypothesized feature, at each layer, for each k
> Note: probe vs sparse probe
- studies the effect of k={1,...8} (k=1 is single neuron)
> An excellent discussion on polysematicity and interference: ... we found many individual neurons which were almost perfectly discriminating. However, after inspecting the activations across a much wider text corpus, we observe these neurons activate for a huge variety of unrelated n-grams, a classic example of the well known phenomena of polysemanticity. Superposition implies polysemanticity by the pigeonhole principle—if a layer of n neurons reacts to a set of m ≫ n features, then neurons must (on average) respond to more than one feature. This example also underscores the dangers of “interpretability illusions” caused by interpreting neurons using just the maximum activating dataset examples [72]. A researcher who just looked at the top 20 activating examples would be blind to all of the additional complexity. While inconvenient for interpretability researchers, polysemanticity is also problematic for the model, as it causes interference between different features [4]. That is, if 70M.L1.N111 fires, the model gets mixed signals that both the “prime factors” feature and the “International Coven” feature are present.

[space and time in LLM]
- probe on last entity token of each layer (layers analyzied individually) with target of either lat/lon or time
- details:
    - adding to the prompt 

[universal neurons]


## Linear Representation Hypothesis
### [concept algebra]
- Y: set of images, 
- X: set of prompts, 
- C: set of latent variabels used to generate X from Y, st $P(y \mid X = x) = \int P(y|C = c)P(C=c|X=x)dc$
- C is complicated so we introduce Z that's C-measurable. So Z maps C to Z which is the σ-algebra of ℤ which is the set of concepts (that's easier to work with than the set C)
- now instead of using P(c|X) which describes how prompts induce latent distribution, we use P(c|Z). To define the situation in which information of Z is same as that of X, we define the notion of "sufficency". A set of concepts ℤ1,...ℤk is sufficient for a prompt X if 
- $p(y |X=x) = \sum_{z_{i:k}} p(y | z_{1:k} )p(z_{1:k} | X=x)$ note how the integral over C becomes sum over Z 

### [linear representation]

### Geometry of Categorical and Hierarchical Concepts
Previous: binary concept with natural contrasts as direction in rep space 
many natural concepts don't have contrasts
features as vectors and representation of concepts as polytopes in rep space



# Prompt Tuning
## Evolution of Techniques
### AutoPrompt
- dot gradient on prefix with word embedding to find k top tokens close to the gradient. Then update from the k tokens with the one that gives best result.

### P-Tuning
- BERT continous prompt with MLP pormpt encoder on NLP tasks. 
- prompt tuning can further improve fully fine tuned models

### Prefix Tuning
- ![](/images/prefix-tuning.png)
### [Scaling Law](https://arxiv.org/pdf/2104.08691)
- prompt tuning converge in GLUE score to full finetuning as model size increases
- 5 to 20 prefix token length might be optimal. But the number decreases with larger model size. At 10b, one token prompt achieves comparable performance.


### RLPrompt

## Interp
### Prompt Waywardness
- for any discrete target prompt p_d, there exists a continuous prompt p_c such that: 1. p_c's nearest neighbor projection is p_d and 2. loss is similar with optimal p_c*
- ![](/images/prompt-wayward-1.png)
- Someone, like a big tech company, might offer a task prompt they tuned but includes malign behavior. You can't tell this because projection might show benign tokens ![](/images/prompt-wayward-2.png)

### Soft prompt might be a bug, not feature
- soft prompts occupy regions in the embedding space that are distinct from those containing natural language. Blue is soft red is natural prompt. ![](/images/soft-prompt-dist.png)
- cosine or L2 nearest neighbor projection reduces task acc to 0
- soft prompts are robust to magnitude reduction but sensitive to direction perturbation >30 degree (99.4% natural prompts cluster in direction, meaning they are 30 degrees near their nearest neighbor). Natural prompts are robust to both.

### Is Continuous Prompt a Combination of Discrete Prompts?
- Decomposing Soft Prompt to Combination of Interpretable Natrual Prompts 
- p is soft prompt, r is weights of length |V|, E is embedding matrix, M is LLM, ⊕ means concat
- train r with 3 losses:
    - distance of reconstruction and soft
    - $E_{x∼D}E_{a∼r,e∼E}[aD_{KL}(M(p ⊕ x), M(e ⊕ x))]$ discrete prompts with larger values should have outputs on downstream tasks that are as consistent as possible with the continuous prompt.
    - sparsity L1 loss on r.
- ![](/images/soft-prompt-decomp.png)

### Toward Human Readable Prompt Tuning (FluentPrompt)
- using energy update on the prefix with fluency constraint (probability of LLM generating the whole prompt sequence)
- the learned prompts increases Surface Form Competition so they do a calibration loss. 
- sample prompts: Kubrick, "The Shining; Paramount, "The Shining; Kubrick\’s "The Man; disappointing.\n\n"
- disappointing.\n\n" is to balance the bias of surface form competition

#### Gradient-Based Constrained Sampling from Language Models (MUCOLA)
- instead of autoregressively geneating sentence, initialize a fixed length output and update all by descendnig the energy function
- $E(y)\;=\;-\,\log P(y\mid x)\;-\;\sum_i\lambda_i\bigl(\epsilon_i - f_i(y)\bigr)$. $P(s)=e^{-E(s)}$ in boltzmann distribution so $E=-\log P(s)$. You can define arbitary  constraint function that takes the output and gives energy.

#### [Surface Form Competition: Why the Highest Probability Answer Isn’t Always Right](https://aclanthology.org/2021.emnlp-main.564/)
- for a multiple choice question, prompting LLM with neutral prompts like "choose from the following ABCD" should result in equal prob for all 4 answers. 

### Sparse Entropy Regularization for RLPrompt Tuning

### Linear Combination of Discrete Prompt Embeddings (MIT)
- select a few prompts and learn a weighting 

# John Hewitt
### Control Task for probing
- Use probes to train on random correspondence tasks and if accuracy is high, the structure found by this probe in desired tasks might not mean the hidden activation itself contain the structure, but that the probe iis powerful enough to learn it. Selectivity = mean acc - mean control task acc
- > "as long as a representation is a lossless encoding, a sufficiently expressive probe with enough training data can learn any task on top of it."
- With popular hyperparameter settings, MLP probes achieve very low selectivity
- linear and bilinear probes are better (26% selectivity vs 4.5%), small internal hidden dim of MLP and small training size improves selectivity

## Backpack
### [Backpack Language Model](https://backpackmodels.science/)
- train senses decomposition (MLP d->4d->d->kxd) and weight assignment function (transformer) end to end for next token prediction. 
- ![](/images/backpack-senses.png)
> Note that this kind of linear decomposition is very different from prompt tuning soft to hard projection. The interpretability of the senses vector here stems from they being the last layer before creating logits. Thus they don't go through the super non-linearity of a transformer as in prompt tuning.
- ![](/images/backpack-control.png)

### [Model editing with canonical example]
- use very few examples to generalize the behavior while avoid distribution shift
- compared LORA, full finetunign and MEMIT, LORA is best
- sense finetuning on backpack, which selects and finetunes a few (≈ 10) sense vectors for each canonical example, and find that it outperforms other finetuning methods

sense tuning
- select important senses: 
- gender bias

questions
- do they mask the attn, because the first word should supposedly give different sense weights depending on later continuations


## Neologism
### Schut AlphaZero knowledge transfer
> The super-human ability of AI systems may arise in a few different ways: pure computational power of machines, a new way of reasoning over existing knowledge, or super-human knowledge we do not yet possess. This work focuses on the last two cases.

Concept
- we define concepts as a unit of knowledge. Unit implies minimality and knowledge implies usefulness towards a task
- in practice, this means a concept can be transferred to another agent to help it solve a task
- we assume concepts are linearly encoded in latent space of NN
- in the RL task, we aim to find concepts (representing reason) that give rise to concepts (representing plans) optimizaing for concepts (goals).

### Model Editing with Canonical Example

### Neologism Position


Thought
- can we train a submodel specifically for different tasks? It could be an sae on just the soft prompt embeddings, it needs many different tasks to span the sae feature space. (Can we sae the embedding and see what the prompts mean)
- in the ensure example, we only trained an embedding, that means the model already has the mechanism to ensure length, 
- what is ensure emebddnig linearly composed of (soft prompt decomposition paper) and its description (inspect paper)
- it's fine for a word to be verbose, because a word is sometimes figurative, every object word would require infnite description for peopple not living in our world. As such, an object also means different set of things for different people, for example, America for a people living in different places at different times mean very different things, yet they can still communicate. 
- are we looking at just words/features or also circuits/ways of thinkng
- potential ideas LM knows but not often used by humans
    - frequency domain arithmatics

# [Geva](https://mega002.github.io/)
### Background
- [Logit Lens](https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens):The logit lens focuses on what GPT "believes" after each step of processing, rather than how it updates that belief inside the step.
- mathematical framework of transformers: the final activation is sum of every layer's contribution. (they believe this means every layer operate on the same embedding space but it's equally possible that each layer uses different embedding)

### Thoughts
- can we study the intermediate residual spaces as we do on embedding or unembedding space. Note the E and U are WORD embedding. Intermediate layers may be sentence or concept embedding.


## Interpretation in Embedding Space
### MLP are Key value pairs
Background
- [Neural Memory (Sukhbaatar et al., 2015)](https://proceedings.neurips.cc/paper_files/paper/2015/file/8fb21ee7a2207526da55a679f0332de2-Paper.pdf). Exactly the MLP memory but non-linearity is softmax, used on RNN. It seems that the only difference btw these neural memory + RNN work and transformer is the attn module, which is highly efficient in mixing information. Sukhbaatar in his work in 2019 also relates the NM with MLP in transformer but didn't invesitigate what those memories are.  

![from leCun's JEPA slides](/images/transformer-as-ram.png)

thoughts
- since there's relu in btw, we can view it as no negative keys, or you only add, not substract. Then there must be anti value vectors for most value vectors in down projection matrix, just like every muscle has an antimuscle. Note that the figure 7 shows non zero activations are 50-10% decreasing wrt layer. "Interestingly, the number of active memories drops towards layer 10, which is the same layer in which semantic patterns become more prevalent"
- relatedly, the cross entropy loss only applies to correct answer so maybe that also underlies why all logits tend to grow, and why correct logit grows fastest instead of others dropping.
- moe
- linear combination of value vectors
- the mlp takes a key and outputs a value. if we ignore the relu, we can think of it as v=Wk. Therefore, a matrix can store associative memory. A matrix is also a linear transformation, and keys are residual vectors, which can also be seen as values from previous layers. Therefore, W linearly maps values to values. It might map a token x to 2x, but y to -y. We could use SVD to see which vectors does W magnify and which it reverses. In transcoder, there's no relu, so the whole thing is actually a linear transformation. I wonder how good a pure transcoder (all MLP's replaced simultaneously) is and if it is good, we can directly understand logit evolution by looking at those matrices. 

### Promotional Sub-update of value vectors to residual
Background
- in key value pair paper, the output of residual itself (before being added to residual) is not very interpretable (though they did discuss individual value vectors). The majority of updates are composition of value vectors. This paper studies these composition (actually no). 
- in that paper, the individual value vectors are hypothesized to be bigram predictions so their experiments start with finding meaningful key vectors first, then check if the corresponding  value vectors match the NEXT token that induces these keys. 

key results
- there are N_layer x d_mlp value vectors. value vectors are indeed human interpretable concepts, as shown by dotting every value vector with E and inspecting top matching tokens. The number of meaningful vectors is twice higher than those from random value vectors (this might be a meaningless analysis since any vector dot E gives a distribution over tokens where top tokens are close)
- FFN updates work in a promotion mechanism, where when the distribution over residual changed after MLP, the change is done by promoting some tokens instead of eliminating others (this might be due to the positive value weight from relu or gelu)

thoughts
- subtract target with value vectors and see if the remaining part matches any token embed


### Everything in Embedding Space
background 
- mathematical framework of transformers' view of QK and OV circuits

key insights
- [left, right, pesudoinverse](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/0550c89b69c99e97dcbf52074e293308_MIT18_06SCF11_Ses3.8sum.pdf)
- **e-dim token space instead of d-dim embedding space**: a sequence of d-dim row vector A (N_seq by d), which appear frequently as residual and intermediate calculation vectors, can be written in terms of embedding (d by N_vocab) and unembedding (N_vocab by d) matrix. We assume $E^{-1}=E^T=U$. Therefore EU=I. AEU=A or A=UEA, let AE=$\hat{A}$ (N_seq by N_vocab), or A=$\hat{A}U$. In other words, any d-dim vector can be matched to the embedding matrix for a distribution over the vocabulary, which can be used to produce expected embedding, or in simpler terms that a vector can be decomposed over basis and added up again.
- now we rewrite attention and FFL as interaction between **tokens** instead of actual residual flows, to achieve input independence. 
- rewrite VO of attention: index i for head. Each head has a WV (d by d_head) and WO (d_head by d). The whole WV dot WO can be seen as WVs dot WOs both concated. $W_{OV}=concatH(W_V^1,...,W_V^i,...,W_V^H)\cdot concatV(W_O^1,...,W_O^i,...,W_O^H)=\sum_i^H W_V^iW_O^i=\sum_i^H W_{VO}^i$ Therefore, when taking in X of (N by d) and attention pattern A of (N by N) we have $concatH(A^iXW_V^1,...,A^iXW_V^i,...,A^iXW_V^H)\cdot concatV(W_O^1,...,W_O^i,...,W_O^H)=\sum_i^H A^iXW_V^iW_O^i=\sum_i^H A^iXW_{VO}^i$. This will be added to the residual and should therefore be interpretable. To see what token it represents we use $A^iXW_{VO}^iE=A^i\hat{X}UW_{VO}^iE$. Attention pattern can be seen as linearly combining each row of X or $\hat{X}$ to produce new rows in embedding or token space. The token embedding is then passed to $UW_{VO}^iE$ which is input independent. It transitions an embedding in token space to another. (why not embeding space directly using WVO?)

### [LM-Debugger](https://github.com/mega002/lm-debugger)
- see before and after top predictions for each layer, following logit lens
- find MLP neurons relavant for any concept, and can turn on those neurons to intervene on the generation

### Function from head params
- $M = E(W_{VO})E^T∈ R^{|V| × |V|}$. Each entry in M is viewed as a mapping score between source and target tokens s, t ∈ V based on W_VO, which signifies how strongly the head promotes it in its outputs.
- ![](/images/head-params.png)

## Interp through patching
### Task vector
### [Patchscope](#patchscope)

### patchscope on soft prompts (Inspect)
- the ICL prompt is to describe the task like "Categorize user feedback into different types: bug report, feature request, compliment" and "Identify the emotion expressed in this text: joy, sadness, anger, fear"
- ![](/images/inspect.png)

### Summary
#### Key
The method is to use prefixes of sentences (eg. I love dogs, I love, I)
- top examples (prefixes) that trigger a key ![](/images/geva-kv-k-eg.png)
- ![](/images/geva-kv-k-stat.png)


#### Key centered value
- for all keys, first find the top triggering example, then find the actual next token of this example, and see if it agrees with the most probable token associated with the value corresponding to this key ![](/images/geva-kv-kv-agree.png)
- ![](/images/geva-kv-top-v-stat.png)

Limitations
- it's possible that for the agreeing key values, they are the same vectors. This is because the residual is already similar to the next token and the keys are therefore also similar to the next token and the value has to be the next token. This is reinforcement and is seen in late layers, so it's suppoorted by the rising aggrement rate at late layers. 
- The shallow keys might be just the embedding of the pattern word. In fact, since the pattern word is the final word, and since it activates the key most stronger than sentence that appends something to the prefix. So their corresponding values might just be a bigram.
- So the complete theory is that MLP's follow a spectrum of bigram to identity. 

#### Value
![](/images/geva-kv-v.png)


#### Superposition
- ![](/images/geva-kv-active-stat.png)

- the sparsity of activations in MLP is expected because the whole idea of superposition relies on a filter, otherwise it becomes PCA. 

#### Promotional Value
- ![](/images/geva-kv-mlp-res-agree.png)



## Factual Recall
### [How transformer recalls idioms](https://arxiv.org/abs/2210.03588)


### Dissecting Recall of Factual Associations




### [Visit](https://github.com/shacharKZ/VISIT-Visualizing-Transformers)


## Vision
### [See conceptor](#conceptor)






# -------- Vision/Multimodal ------------
## Basics
Image processing is "harder" than language because it's more primitive. Fishes have vision, but only humans speak. All language related tasks require only language as input and output. But vision tasks are variable (classification, segmentation, captioning, etc) and input and output are often not images. It's worth thinking what a language transformer and a vision transformer mean in the brain. 

### History
- GANs 2014
- MoCo 2020
- CLIP 2021
- DINO 2021

### ViT
- Image is first split into m fixed size patches
- each patch is embedded with pos encoding as input to transformer
- usually a [CLS] token is prepended 
- after last layer, the CLS position token output will go through a head that gives image class (sometimes they pool image token outputs and drop CLS altogether)

### Architectures
- Dual encoder: CLIP
- Fusion encoder: give image and language related tokens together to transformer
    - cross attention from the start
    - full cross attn from a certain layer on, so early layers are modality specific


### Objective
- moco: ![](/images/moco.png)
- contrastive image pair to learn image representation
- BYOL: non contrastive, two networks with 
- Dino: 
- Masked Language Modeling, like BERT but with image input
- masked image modeling, use dVAE and predict masked emcoding
- masked multimodal modeling (introduced in FLAVA)
- image captioning
- image caption matching 





## Tuning/Interp
Prompt Tuning: In addition to the follow-up works on how to construct better prompting texts, recent works propose to treat the prompts as task-specific continuous vectors and directly optimize them via gradients during fine-tuning.

### Visual Prompt Tuning
Instead of altering or fine-tuning the pre-trained Transformer itself, we modify the input to the Transformer.

- ![](/images/VPT-1.png)
- Note that lienar means just finetune a linear head on the CLS output, it achieves a very good improvement with just 0.02x param; also bias means just finetune all bias terms and it achieves near full finetuing performance with 0.05x param. VPT-shallow has 0.04x param and deep has 0.18x params. ![](/images/VPT-2.png)
- ![](/images/VPT-4.png)
- ![](/images/VPT-3.png)

### MILAN
Given a neuron, MILAN generates a description by searching for a natural language string that maximizes pointwise mutual information with the image regions in which the neuron is active.


## CLIP/cls ViT Interp
### [CLIP SAE](https://www.lesswrong.com/posts/bCtbuWraqYTDtuARg/towards-multimodal-interpretability-learning-sparse-2)
- vit-clip trained a mid layer sae on image-net-1k, lots of visual examples of highest activating images for many features

### [CLIP sae and difussion intervention](https://www.lesswrong.com/posts/Quqekpvx8BGMMcaem/interpreting-and-steering-features-in-images)
- train SAE on clip 
- use the features to intervene on stable diffusion conditioned on image (maybe also works on text), for example, given cat image, encode the image with intervened sae and use the altered embedding as input to diffusion. 

### [Prisma](https://www.alignmentforum.org/posts/kobJymvvcvhbjWFKe/laying-the-foundations-for-vision-and-multimodal-mechanistic)
- open source vision MI toolkit
- good background section on methods in MI and tools, and why vision MI is more nuanced
    - Unlike language models, vision transformers do not have a dictionary-style embedding and unembedding matrix. 
    - Language input is discrete while vision input is continuous. 
    - Vision models typically employ contrastive learning or unsupervised approaches rather than next-token prediction.
- interesting findings
    - feature is much denser in ViT SAE: image distribution is denser? token number is much smaller?
    - model improvement with SAE
- the website shows some cool visuals of their functionality
    - logit lens for CLIP: the emoji means at the specified layer and patch location, directly map that residual activation to output class with the head MLP, kinda similar to logit lens output embedding mapping ![](/images/prisma.png)
    - head anaysis, geometric heads in first layer

### [CLIP head Lens](https://yossigandelsman.github.io/clip_decomposition/)
- ViT-CLIP, heads are added, layers are added, for MSA, contributions from image patches are added, so the image-text joint repr is sum over H heads, L layers and N patches. 
- to interpret each late layer head's function, find prompts that explain the most variablity of the output of the head, by actually feeding inputs and collect heads' outputs and project the variance onto the proposed span of concept embeddings. Maximize the projection
- ![](/images/clip-lens.png)

### [CLIP Neuron lens](https://yossigandelsman.github.io/clip_neurons/)
- everything on cls token
- neuron means the 1-d output subspace of an MLP neuron, ie, a column of the value matrix
- each neuron's first order contribution to the image is too small, so use second order, which means the sum of the neuron's effect on all subsequent layers all MSA heads. 
- the second order effect is approx rank 1. Using orthogonal matching pursuit, decompose the second order effect vector to principle words from common words. 
- ![](/images/clip-neuron-lens.png)

### [Splice]
- CLIP embedding as linear combination of sparse concepts. 
- ![](/images/splice.png)

procedure
- Mine the most common 1- and 2-word phrases (“coffee,” “birthday party,” etc.) from the LAION-400M captions.
- Encode each phrase with the CLIP text encoder and mean-center + re-normalize (to handle the known “image vs. text cone” gap).
- Stack your centered & normalized concept vectors as columns in a matrix C.
- You want to find a nonnegative weight vector w (of length |vocab|) so that Cw points back to z—but with as few nonzeros as possible.
- $ \min_{w \ge 0}\;\|C\,w - z\|_2^2 \;+\; 2\lambda\,\|w\|_1,$
> psychology shows 20 concepts is best for one image/sentence



## Difussion
### Basics
Stable Diffusion
- the noise latents are fixed dimension matrix of N by d. Each latent vector has information over the whole image
- The denoising UNet maps intermediate representations to query vectors, the CLIP encodiing of prompt to key and value vectors.
- ![](/images/sd.png)

Diffusion Transformer
- ![](/images/dit.png)

Inversion-reconstruction

### [Kandinsky](https://github.com/ai-forever/Kandinsky-2)
- ![](/images/kandinsky.png)


### [ControlNet](https://github.com/lllyasviel/ControlNet)
- [](/images/control-net-2.png)

### [DAAM](https://github.com/castorini/daam)
- what words contribute to what pixels
- stable diffusion uses CLIP text embedding as k and v to answer q from images. For a specific token we can analyze the attention matrix's  column and see what queries it answered. 
- each unet level's attention map is bicubic interpolated to highest resolution and added to create the segmmentation map
- ![](/images/daam.png)

### [Diffussion lens](https://tokeron.github.io/DiffusionLensWeb/)
- use per layer activations from text encoder (apply final layer norm) to genrate image. 
- ![](/images/diff-lens.png)

### [Diffusion steering]
- use per layer activations from image encoder to genrate image. 
- ![](/images/diff-steering.png)

### [conceptor](https://hila-chefer.github.io/Conceptor/)
- in stable diffusion, decompose a text prompt encoding into linear combination of vocab embedding ($w^*=\sum^V a_i w_i$), weights optimized per concept with small MLP. 
- ![](/images/conceptor.png)

### [CLIP sae and difussion intervention](https://www.lesswrong.com/posts/Quqekpvx8BGMMcaem/interpreting-and-steering-features-in-images)
See CLIP section above

procedure
- pass a prompt (like "apple") to CLIP to get a concept embedding 
- run SD to get 100 images
- use the 100 images to run the diffusion reconstruction loss on noised images conditioned on w*, so w* faithfully steer the diffusion process towards the images instead of simply minicing the prompt embedding
- after we trained the MLP, we can decompose a single image. We use the seed if that image and remove one w at a time to generate a new image, then we compare CLIP of the two images and remove w if CLIP score is below 95. Do this for all w. Not clear if they follow a greedy alpha approach.
- ![](/images/conceptor-2.png)

## RL
### Minecraft
Steve 1: https://arxiv.org/pdf/2306.00937 
Interpretable steve 1: https://arxiv.org/pdf/2407.12161

# ------- Test Time -------
> Research on “dual process” models suggests that people have two modes in which they engage with decisions – a fast, automatic, unconscious mode (“System 1”) and a slow, deliberate, conscious mode (“System 2”)

> A genuine problem-solving process involves the repeated use of available information to initiate exploration, which discloses, in turn, more information until a way to attain the solution is finally discovered.—— Newell et al.






# Thoughts
the decision tree can be input to a system 2 transformer but a normal LLM might do just as well









# ------- Neuro oriented -------


# MIT
## Fedorenko
### 





# James 

## [Disentanglement with Biological Constraints](https://arxiv.org/abs/2210.01768)
## [Transformer and hippocampus](https://arxiv.org/abs/2112.04035)
## [Grid Cells from Minimal Constraints](https://arxiv.org/abs/2209.15563)
## [Tolman-Eichenbaum Machine](https://www.cell.com/cell/fulltext/S0092-8674(20)31388-X)


# Columbia
## Temporal Straightening
### BG
- they first did experimental thing on humans to infer the perceptual curvature of sequence of images
- second paper is on V1 neurons of monkeys

### Large language models implicitly learn to straighten neural sentence trajectories to construct a predictive representation of natural language
The critical insight comes from vision: because a sequence of visual inputs to the retina evolves in a nonlinear manner, and are difficult to extrapolate, visual system performs a series of transformation to make them easier to predict. The representation of input sequence is transformed to result in straighter the trajectory in the internal state,

Curvature is calculated as angle which comes from arccos of dot product

Thoughts
- First the middle layer as representation of current sequence can support lots of other work. Most semantic steering and those meaniningful circuit effects happen at mid-layers. 
- It's interesting that the middle layer residuals are similar (small curvature means small dot product) because they are all there are to represent the sequence, and they will each go on to evolve their corresponding next tokens. But in the representation view this is not surprising since adding one word should not change the representation of the sequence too much. 

## Issa
### Brain-Score
![](/images/brain-score.png)
Electroarray in monkey and record when seeing image. Linearly map btw ANN intermediate layer activation and the moonkey recording and check correlation.



# Thoughts
## Features
- concepts are functions that when all orthogonal concepts operate on the state of the world, the concept of interest is invariant, ie, concept(new states)=concept(old states)
- the state of the world is largely random, we can imagine all states of the world through all times laid out before us. Many of them will 
- the metaphysical concept, or pure forms of the world, are either physical transformations of the environment under laws of dynamics, or transformations of the input stimuli to an intelligent system as a result of the system's state change. For example, the physical law that moves the apple from above to ground preserves the notioin of the apple, no matter its altitude. The change of viewpoint, as a result of your own movement, will similarly preserve the concept of objects withiin your view

### Coding Effieciency
There's an inherent tradeoff between feature based and exact matching based memory. Exact matching is fast. For example, when typing, we remember the exact sequence of movements leading to a word or a subword. Most of us actually don't remember the keyboard at all. We don't know what the second row's second key is. The keyboard is feature. We have traded this off for speed. 

When coding 16 objects with 4 bits or with 16 bits. The 16 bits system is fast. The 4 bits system needs to be resolved  


## Information
Information is anything that decreaes entropy. As in physics, the definition of entropy is subjective. It depends on what you want to know and what you can keep track of. 

Words in different languages can carry similar amount but different distribution of information. By reading or seeing or hearing something, the  change of your state are surely different, though they can change the same amount of entropy, depending on how you map state to entropy. 

Abstract ideas have low information, but when you want multiple pieces of information/systems, their underlying state distributions might overlap, and now an abstraction carries more information on what you want to know, ie, the multiple things, each reduces some ambiguity by the said abstract information.

# By Concepts
## Identifying Feature
activation patching 
- a form of ablation and attribution patching approximates activation patching

direct logit attribution 
- approximates activation patching in a certain layer


## Feature Steering/Model Editing
### Feature Steering (Change activation not weight)
[function vector] 
- within-task: activation patching and find attention heads by measuring causal indirect effect of last token attn activations. 
- cross-task: take highest average indirect effect heads' output across samples for a task and add it to another task.
- Giving a sentence to GPT and ask it to continue vs giving the same sentence but inject the FV. ![](/images/fv-1.png)
- ![](/images/fv-2.png)
- First copy means the task is to output the first word in the list. ![](/images/fv-3.png)

[steering vector](https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector): 
- run a concept like "golden gate bridge" and get some activations mid-layer and add those to other runs at that location (first tokens)

[control vector](https://vgel.me/posts/representation-engineering/#So_what_exactly_is_a_control_vector?)
1. run counterfactual pairs 
2. collect last token states at every layer
3. diff the average states 
4. PCA

### Model Editing (Change weight not activation)
[ROME]
- Given a dataset X and corrupted dataset X* (eg, The space needle is in, The space neeble is in; actual corruption technique is diverse and task specific at the moment)
    1. run the model on X, store activations and prob of correct answer
    2. run the model on X*, store activations and prob of correct answer
    3. run the model on X*, restore activation from running X on desired positions, store prob of correct answer
    4. average the effect: 

[MEMIT]


## Identidying Circuit/Mechanism
### Relation
[Linear encoding of relation](https://lre.baulab.info/)
- Given a relation r such as plays the instrument, a linear relational embedding is an affine function $LRE(s) = W_r(s) + b_r$ that maps any subject representation s in the domain of the relation (e.g. Miles Davis, Carol Jantsch) to the corresponding object representation o (e.g. trumpet, tuba).
- Attribute Lens ![](/images/attr-lens.png)


# Others
- [momenntum gd and dynamics](https://distill.pub/2017/momentum/)

# Neuro
[how brain selects memory](https://www.youtube.com/watch?v=ceFFEmkxTLg)
- sharpe wave ripple at night selects most significant memory during day (Matthew effect)
> my note: keep in mind that it's still possible that no memory is ever really lost as shown by recalling distant non significant random memory
- during sleep, neocortex not receiving real stimuli and listens for hippocampus stimuli thus transfer memory from hippo to neocrotex
- during wakefulness infrequent sharp wave ripples tag memories for later  consolidaiton

## Evolution constraint
[David Marr, A theory for the archicortex](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.cs.cmu.edu/afs/cs/academic/class/15883-f17/readings/marr-1971.pdf)