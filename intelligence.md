# Basics
## Transformer
- $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V=[V^T\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)]^T$
- input $(N_{\text{tokens}}, N_{\text{dim}})$
- $W_Q=W_K=W_V:(N_{\text{dim}}, N_{\text{dim}})$
- $Q=K=V:(N_{\text{tokens}}, N_{\text{dim}})$
- $QK^T \in \mathbb{R}^{N_{\text{tokens}} \times N_{\text{tokens}}}$
- concat heads->output projection->add&layer norm->mlp->add&layer norm
- add&layer norm is post-norm and pre-norm is also used.

### Attention
MHA

MQA

GQA

### MLP
MOE

### Language Modeling
- Pure embedding unembedding means bigram
- one layer attn means skip trigram where instead of using 2 words to predict the next word, the model uses the current word combined with a second word anywhere in the context to predict the next word. In theory, if KVQ are arbitary functions, one layer attn can support n-gram where n is any integer. But for linear KVQ, the skip trigram is most effective.
- two layer attn 

## Neuron & Features
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


# MI (Anthropic)
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
### [First Circuit Analysis](https://transformer-circuits.pub/2021/framework/index.html)
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

### [Sparse Autoencoder](https://transformer-circuits.pub/2023/monosemantic-features/index.html)
Crucially, we decompose into more features than there are neurons. This is because we believe that the MLP layer likely uses superposition to represent more features than it has neurons (and correspondingly do more useful non-linear work!)

![](/images/arena-sae-diagram-2.png)

# Patching
## Intuition
### Model the world
The practice of "knocking out" is ancient for experimental scientists. We knock out genes or generals in war to see the effects. As a living thing, we want to model the world. To model the world, we sometimes disentangle the building blocks (with varying scale) and model them individually so the total effects can be summed from the parts. Since models benefitial for living are inherently causal (we want to be sure that a snake causes the poisoning), we developed the tool of knocking out to study causal effects of parts of the system.

One problem is that we sometimes are able to knock sth out and observe something, but can't observe what hapended in between (there are many reasons why we can't observe everything but think about chaos, quantum effects and cost). This means we can't model the actual causal effect (direct effect in literature). If we change location or introduce a small change to the system our model might go wrong. The indirect effect must be removed from the total effect when we run the experiment.

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
- The author tries to find a minimal circuit that completely describes a task. They used activation patching first. First thing to know is that activation patching (AP) requires a clever selection of counterfactual prompts. Any element of importance found by AP is necessary and sufficient for the hypothesized behavior. 
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



### LOCALIZING MODEL BEHAVIOR WITH PATH PATCHING
- nodes are functions and edges are values
- Formally, a hypothesis H is a tuple (G, δ, S, D) where δ: Y^2→ R is some measure of dissimilarity. S is a set of “important nodes”, G \ S are the unimportant nodes, and D is a joint distribution over (x_r, x_c) pairs (counterfactual data provider).
- The strictest version of what it means for H to hold is that $δ(G(x_r), G_H(x_r, x_c))$ is exactly zero everywhere on D. We use AUE, averaged unexplained effect, which is expectation of the above formula.





## MIT

[FINDING NEURONS IN A HAYSTACK : CASE STUDIES WITH SPARSE PROBING]
- find k neurons that corresponds to human concepts
- studies the effect of k (k=1 is single neuron)
- probing:
    - cons: 1) probing requires hypothesis (need to manually select features and corresponding counterfactual pairs of inputs) 2) probing is correlational

[space and time in LLM]
- probe on last entity token of each layer (layers analyzied individually) with target of either lat/lon or time
- details:
    - adding to the prompt 

[universal neurons]

[concept algebra]

# Linear Representation Hypothesis
## [linear representation]

## Geometry of Categorical and Hierarchical Concepts
Previous: binary concept with natural contrasts as direction in rep space 
many natural concepts don't have contrasts
features as vectors and representation of concepts as polytopes in rep space

# James 

## [Disentanglement with Biological Constraints](https://arxiv.org/abs/2210.01768)
## [Transformer and hippocampus](https://arxiv.org/abs/2112.04035)
## [Grid Cells from Minimal Constraints](https://arxiv.org/abs/2209.15563)
## [Tolman-Eichenbaum Machine](https://www.cell.com/cell/fulltext/S0092-8674(20)31388-X)


# Intrinsic Model Vectors
### (Logit Lens)[https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens]
The logit lens focuses on what GPT "believes" after each step of processing, rather than how it updates that belief inside the step.

thoughts
- can we study the intermediate residual spaces as we do on embedding or unembedding space. Note the E and U are WORD embedding. Intermediate layers may be sentence or concept embedding.

## [Geva](https://mega002.github.io/) and the Israeli gang
### Background
- logit lens
- mathematical framework of transformers

### MLP are Key value pairs
Background
- [Neural Memory (Sukhbaatar et al., 2015)](https://proceedings.neurips.cc/paper_files/paper/2015/file/8fb21ee7a2207526da55a679f0332de2-Paper.pdf). Exactly the MLP memory but non-linearity is softmax, used on RNN. It seems that the only difference btw these neural memory + RNN work and transformer is the attn module, which is highly efficient in mixing information. Sukhbaatar in his work in 2019 also relates the NM with MLP in transformer but didn't invesitigate what those memories are.  


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

### [How transformer recalls idioms](https://arxiv.org/abs/2210.03588)



### Everything in Embedding Space
background 
- mathematical framework of transformers' view of QK and OV circuits

key insights
- [left, right, pesudoinverse](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/0550c89b69c99e97dcbf52074e293308_MIT18_06SCF11_Ses3.8sum.pdf)
- **e-dim token space instead of d-dim embedding space**: a sequence of d-dim row vector A (N_seq by d), which appear frequently as residual and intermediate calculation vectors, can be written in terms of embedding (d by N_vocab) and unembedding (N_vocab by d) matrix. We assume $E^{-1}=E^T=U$. Therefore EU=I. AEU=A or A=UEA, let AE=$\hat{A}$ (N_seq by N_vocab), or A=$\hat{A}U$. In other words, any d-dim vector can be matched to the embedding matrix for a distribution over the vocabulary, which can be used to produce expected embedding, or in simpler terms that a vector can be decomposed over basis and added up again.
- now we rewrite attention and FFL as interaction between **tokens** instead of actual residual flows, to achieve input independence. 
- rewrite VO of attention: index i for head. Each head has a WV (d by d_head) and WO (d_head by d). The whole WV dot WO can be seen as WVs dot WOs both concated. $W_{OV}=concatH(W_V^1,...,W_V^i,...,W_V^H)\cdot concatV(W_O^1,...,W_O^i,...,W_O^H)=\sum_i^H W_V^iW_O^i=\sum_i^H W_{VO}^i$ Therefore, when taking in X of (N by d) and attention pattern A of (N by N) we have $concatH(A^iXW_V^1,...,A^iXW_V^i,...,A^iXW_V^H)\cdot concatV(W_O^1,...,W_O^i,...,W_O^H)=\sum_i^H A^iXW_V^iW_O^i=\sum_i^H A^iXW_{VO}^i$. This will be added to the residual and should therefore be interpretable. To see what token it represents we use $A^iXW_{VO}^iE=A^i\hat{X}UW_{VO}^iE$. Attention pattern can be seen as linearly combining each row of X or $\hat{X}$ to produce new rows in embedding or token space. The token embedding is then passed to $UW_{VO}^iE$ which is input independent. It transitions an embedding in token space to another. (why not embeding space directly using WVO?)

### [Visit](https://github.com/shacharKZ/VISIT-Visualizing-Transformers)


### [Diffusion](https://hila-chefer.github.io/Conceptor/)

# Thoughts
## Features
- concepts are functions that when all orthogonal concepts operate on the state of the world, the concept of interest is invariant, ie, concept(new states)=concept(old states)
- the state of the world is largely random, we can imagine all states of the world through all times laid out before us. Many of them will 
- the metaphysical concept, or pure forms of the world, are either physical transformations of the environment under laws of dynamics, or transformations of the input stimuli to an intelligent system as a result of the system's state change. For example, the physical law that moves the apple from above to ground preserves the notioin of the apple, no matter its altitude. The change of viewpoint, as a result of your own movement, will similarly preserve the concept of objects withiin your view


# By Concepts
## Feature/Model Steering
activation patching 
- a form of ablation and attribution patching approximates activation patching

direct logit attribution 
- approximates activation patching in a certain layer

function vector: 
- within-task: activation patching and find attention heads by measuring causal indirect effect of last token attn activations. 
- cross-task: take highest average indirect effect heads' output across samples for a task and add it to another task.

[steering vector](https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector): 
- run a concept like "golden gate bridge" and get some activations mid-layer and add those to other runs at that location (first tokens)

[Steering vector](https://vgel.me/posts/representation-engineering/#So_what_exactly_is_a_control_vector?)
1. run counterfactual pairs 
2. collect last token states at every layer
3. diff the average states 
4. PCA

# Others
- [momenntum gd and dynamics](https://distill.pub/2017/momentum/)


# Neuro
[how brain selects memory](https://www.youtube.com/watch?v=ceFFEmkxTLg)
- sharpe wave ripple at night selects most significant memory during day (Matthew effect)
> my note: keep in mind that it's still possible that no memory is ever really lost as shown by recalling distant non significant random memory
- during sleep, neocortex not receiving real stimuli and listens for hippocampus stimuli thus transfer memory from hippo to neocrotex
- during wakefulness infrequent sharp wave ripples tag memories for later  consolidaiton