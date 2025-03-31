



# Embedding Space
## Space
### Physics


### Model


### Human Language Analogy

## Representation 
### Internal Thoughts
I used to think that there are ways to let the model "give their thoughts" by translating the intermediate activations to something interpretable. The notion of "thoughts" needs to be carefully defined. When we think about thoughts, we usually mean the explicit thoughts, the ones that can directly be spoken out or drawn down. We rarely include the subconscious thoughts when we talk about thoughts as in "what are you thinking" or "what're your thoughts". Thus from this definition the output of the model are the thoughts instead of any middle representations. 

What actually corresponds to the hidden representations are also the hidden things in our brain. When you, for example, think about Augustus when seeing the word Rome, we could study how exactly the thought came up by studying the implicit activations that leads from Rome to Augustus. The problem is we might not be able to interpret them. Most human interpretable concepts are, not surprisingly, human words. Thus the process that leads from one word to another can only be understood as a transformation of words. 

We thus ask how exactly can we mechanistically explain a thought. An intuitive approach is to identify 2 things at every step of the transformation: what are the major laws governing the transformation and what are the major objects influencing the object of interest, ie, the object being transformed. Therefore, it's possible to actually just study the transformation as a list of words where each word is formed by the previous word interacting with various other things. Note that word is a simplified notion, it should be a list of words/concepts/notions (think of them as decorators to the first word or think of one word as superposition of many words). The tricky part is to identify the strongest interaction. In image processing, we could visualize every filter but it's hard to give a mathematical explanation of exactly an image is classified as say an apple. 

## Feature/Concepts

### Isomorphism
we imagine an experiment where a perfect model (biological or artificial) perceives an input. We first present it with a black square and remove it, and record the activation at one layer. Now we have 2 representations correspsondig to yes or no to the question "is there a black square". We use binary concepts for simplicity. Now we present it with a red square, and compare the representation of black square, they should be different. We further assume no superposition, and that there is exactly one neuron whose binary reading inndicates presence of a feature (no polysemanticity). We can see the multiple nature of feature representation. We can define a feature as:
1. the activatoin value of a specific output neuron
2. the set of inputs that gives a specific output neuron a specific value
3. 

> Necessity and suffficiency of a circuit for detecting a feature: the ability of a model to detect a feature means the model can perfectly gives yes to inputs that contain a feature and no to those that don't. If we remove a part of the model and it's still capable of that, we say the remaining model is sufficient for detecting the feature. If we remove a part of the model and 

### Definition of concept
> What is an apple: when we pass images of apples to the model, the model will invariably identifies an apple (assume a "perfect" model), and when we pass non-apples, the model will invariably output something other than apple. Assume that apple is a concept that cannot be further decomposed (you can decompose a concept hierachiically so a king would be something like a male with supreme power in a kingdom), and the model (input image and output yes or no to all concepts) can perfectly identify every non-decomposable (leaf) concepts, then the concept of apple means we could change every other concept (finding images that give different outputs) 

> Duo or Uno

> Case study of IOI circuit: 

## Thoughts
- If two layers share the exact same embedding space, then a concept vector from either layer should represent the same concept in another. For example, just by averaging tokens related to gender we should be able to find a gender vector and be able to add it to any layer and observe a gender related output effect. (this is true)

### Learnable latent
the learned latent from graphics work (usually MLP), the CLIP embed of stable diffussion, and similarly the latent in GANs, can be seen as an early feature vector that steer the output interpretably. 

### Fundamental problem of feature
The problem with analyzing states as if they are physical objects is that the intermediate states are hard to interpret. It's not likely to build a table of such elements for reference. This is also a reason for excitement in neural science and CNN as they present intermediate states (neural patterns in both cases) that are interpretable. Language is different in that almost all human concepts are already there. The intermediate layers should not be any more "interepretable" than the embedding.
> We could see the abstract features as extending the unembedding matrix. A fundamental limit of the logit lens is that tokens are not very interepable. For example, Harvard is broken up into Har and vard, so a logit lens will see a Harvard related activation as Har. This happens at numerous scales and we could extend the embedding matrix indefiniitely to have features like "a political figure who is tall and young". But this will be inferior to SAE. 

Adding to the unexplanabiility of intermediate activations is the interference or non orthoganality of features. If we got an activation and want to decompose it to its feature dimensions, we are basically solving for Ax=b were b is the activation and A is the feature vectors. There could be infinite linear combinations of the features that give b, not to mention errors or inherent uninterpretable directions. Tha'ts why SAE might be the best we have because it decomposed activations to high dimensional orthogonal directions. 

> word2vec like embedding is not effective in identifying homographs/homonyms (word with multiple meanings) as the representation is regression to a "mean" vector. We can study how homonyms is embeded and propagated in transformer


## Experimennts

embedding space feature direction is the same feature direction in all layers
- checked the gender direction and works well
- a "medieval-modern" direction failed

logit lens on input and output compare agaisnt input and output tokens (2 x 2 per token)
- this is to test if the information about previous tokens are encoded directly by directions used in embedding space.
- "apple tree" will make the the tree token at mid layer contain some apple
- "Uncle Peter was a thief but he loved us, so we". study how the "we" token gradually accumulated things from thief and love. Similarly, "There is a big white cherry tree, it..." it will contain "big white cherry tree" and using intermediate activation of it alone can make the model generate things simialr to whole prompt. 


"We are traveling in Paris/Beijing/London/Moscow/Washington and visited the famous" 

"Mary/Alice/Anne and John/Bob/Chris went to the store. John gave a bottle of milk to"



## Universal Representation
### Human Language Analogy





## Information Theory
the information content on the first look is the same across layers. It would be truly the same if the last layer can also retrodict the first token. 



when people do iratioinal things this is similar to waking up feeling everything is useless vs everythinig is good. there are fundamental effectors in brain where higher thinkng connects to. Some conn are temp and some are heavilly modulated by transmitters


# Steering
[ways of implementing basic activation steering](https://www.lesswrong.com/posts/ndyngghzFY388Dnew/implementing-activation-steering)
- compute steering vector: average; PCA; linear classifier (which is a vector of same size and used as steering vec)
- trasformer lens results are not the same as original so be careful
- nnsight might be the best: 
```py
from nnsight import LanguageModel

model = LanguageModel("gpt2")

# Define the steering vectors
with model.invoke("Love") as _:
   act_love = model.transformer.h[6].output[0][:, :, :].save()
with model.invoke("Hate") as _:
   act_hate = model.transformer.h[6].output[0][:, :, :].save()

steering_vec = act_love - act_hate

# Generate text while steering
test_sentence = "I think dogs are "
with model.generate() as generator:
   with generator.invoke(test_sentence) as _:
       model.transformer.h[6].output[0][:, :2, :] += steering_vec[:, :2, :]

print(model.tokenizer.decode(generator.output[0]))
```
- maybe do sae on embedding with equal importance and use the neuronpedia techniques to study the features