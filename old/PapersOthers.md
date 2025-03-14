# Face
- [Unity The making of Enemies](https://www.youtube.com/watch?v=a0vAWyZXMWg&list=PLX2vGYjWbI0Q4rTRGHz9K71F4HnDUvGiF&index=2)
- [Ziva Face Trainer](https://zivadynamics.com/ziva-face-trainer)
- [Blender Facebuilder](https://medium.com/keentools/facebuilder-for-blender-guide-cbb10c717f7c)
- [Snap Face Mesh](https://docs.snap.com/lens-studio/references/templates/face/face-mesh#guide)

# Neural Network
## Synaptic

## Pruning
### LOTTERY TICKET HYPOTHESIS
Train a network, prune low magnitude weights, revert the rest to initialization state, train again, iterate several times.

When randomly reinitialized, winning tickets perform far worse, meaning structure alone cannot explain a winning ticket’s success.

One possible explanation for this behavior is the good initial weights are close to their final values after training—that in the most extreme case, they are already trained. However, experiments show the opposite—that the winning ticket weights move further than other weights.

we hypothesize that the structure of our winning tickets encodes an inductive bias customized to the learning task at hand. Cohen & Shashua (2016) show that the inductive bias embedded in the structure of a deep network determines the kinds of data that it can separate more parameter-efficiently than can a shallow network

#### Early Bird Tickets
we discover for the first time that the winning tickets can be identified at a very early training stage, which we term as Early-Bird (EB) tickets, via low- cost training schemes


--------------------------------------------
# NLP
## RNN
### Inside RNN
#### [VISUALIZING AND UNDERSTANDING RECURRENT NETWORKS](https://arxiv.org/pdf/1506.02078.pdf)
"For instance, one cell is clearly acting as a line length counter, starting with a high value and then slowly decaying with each character until the next newline. Other cells turn on inside quotes, the parenthesis after if statements, inside strings or comments, or with increasing strength as the indentation of a block of code increases."

### LSTM
<img width="400" alt="Screen Shot 2023-01-15 at 2 04 57 PM" src="https://user-images.githubusercontent.com/36484215/212564313-a5ba56f3-a8be-487a-8759-8ee30f5c5992.png">

- memory is like the real memory. previous output and current input update memory. after update, memory, previous output and current input all together produce new output. new output is recursed back to the program for further thinking.
- theoretically, lstm is just like a brain.
- note that both hidden state/output and memory are vectors. forget gate has same dimension as memory and operates elementwise on memory (each scalar in memory vector controlled seperately). new memory (candidate x input gate) also has same dimension as memory and control change into memory elementwise.

## Word Embedding
### Word2Vec & GloVe
![](/images/word-2-vec.png)

### ELMo: Context Matters
- A word has multiple meanings depending on context
- Instead of using a fixed embedding for each word, ELMo looks at the entire sentence before assigning each word in it an embedding. 
- It uses a bi-directional LSTM trained on language modeling task

## Attention 
### Transformer
[illustrated transformer](https://jalammar.github.io/illustrated-transformer/)

[counting transformer parameter](https://stackoverflow.com/questions/64485777/how-is-the-number-of-parameters-be-calculated-in-bert-model)
![](/images/transformer-encoder.png)
![](/images/transformer-dimensions.jpg)
![](/images/transformer-decoder-attention-mask.png)
Note that in inference, we keep key and value of previously generated tokens and only do calculation on the new tokens' row since all other rows won't change with this new token. so the decoder is essentially one word in one word out.

#### **Relationship with MLP**
When we go from the input Lxd to concated multihead attention output Lxd, we can just replace the attention mechanism with a mlp whose every layer has input size L\*d and has L\*d neurons. We first need 3 parallel such layers to compute q,k,v. here each row in the output should only concern each row in the input (tokens lead to their own questions and answers). So like in CNN, replacing local convolution with MLP means big MLP with lots of wasted neurons. Then we concatnate output of Q and K and pass that to a 2\*L\*d input, L\*d neurons layer to get self attention. This is a special layer in that it only contains 0 and 1s. (representing matrix multiplication as a fixed matrix multiplication of concated inputs and a "rule matrix") Next, we soft select V which is another matrix multiplication. 

In conclusion, transformer can be represented by an extremely big MLP, just like CNN. But we use a powerful inductive bias to fix most of operations.

#### **Relationship with CNN**
The receptive field of each word in transformer is the whole input sequence. This might seem weaker than CNN's local focus, but the whole input sequence is selectively attended. So in effect, it sees everything but focus on a potentially small area of interest, which makes it more powerful than local focus.

This also means that each output of attention in transformer can be seen as a feature representation like those in layered CNN.

#### **Relationship with Neuron (Hypothesis)**
If we replace transformer with an equivalent MLP and omit all 0s, we can get a sparse MLP which resembles a not too large neural network.

#### NLP's ImageNet moment has arrived
> In NLP, models are typically a lot shallower than their CV counterparts. Analysis of features has thus mostly focused on the first embedding layer, and little work has investigated the properties of higher layers for transfer learning. Transformer is paradiam shifting: going from just initializing the first layer of our models to pretraining the entire model with hierarchical representations. If learning word vectors is like only learning edges, these approaches are like learning the full hierarchy of features, from edges to shapes to high-level semantic concepts. 
> Transformer employed pretrained language models to achieve state-of-the-art on a diverse range of tasks in Natural Language (https://www.ruder.io/nlp-imagenet/)

#### Totally Understood Language?

### BERT
- Encoder only.
- Trained on dataset of 3.3 Billion words. 64 TPUs for 4 days
- Trained with Masked Language Model (50%) and Next Sentence Prediction (50%)
- Mask token is not 0, it's like any other learned token embedding
http://jalammar.github.io/illustrated-bert/
> marking the beginning of a new era in NLP

![](/images/bert-tasks.png)
![](/images/bert-feature-extraction.png)

### GPT (1,2,3)
- Decoder only
- Removed the encoder decoder cross attention block. Only major difference is mask (forward mask vs learned [MASK] token embedding).
- Trained autoregressively. In translation task, input both languages and mask target language. In summurization, input both article and summary and mask summary. In these senarios, decoder only is almost equivalent to original encoder decoder.
- 117M->1.5B->175B parameters

![](/images/decoder-only-transformer-translation.png)

### Understanding Transformer Related
#### Transformer Feed-Forward Layers Are Key-Value Memories & [Persistent Memory + Attention](https://arxiv.org/pdf/1907.01470.pdf)
- FFNN takes up 2 third of parameters.
- embedding_dim x 4*embedding_dim matrix
- each column is a key
- the second 4*embedding_dim x vocab_size matrix holds values
- each row is a distribution over all words
- If we replace FFNN with a persistent "memory matrix", where key and value from which is cross attentioned with query from attention block, we get similar results.




--------------------------------------------
# Multimodal
## Image Captioning 
### Encoder-Decoder
#### Karpathy


### Transformer
#### CLIP
![](/images/clip.png)
Both encoders are pretrained transformers. Text encoder is GPT like while image encoder is based on a vision transformer. Training involves cross-modal similarity loss and weight updates jointly on the two encoders


#### [Multimodal Neurons](https://openai.com/blog/multimodal-neurons/)
Methods to investigate function of neuron: *feature visualization*, which maximizes the neuron’s firing by doing gradient-based optimization on the input, and *dataset examples*, which looks at the distribution of maximal activating images for a neuron from a dataset.

## Misc
### 2D
#### [Semantically-Aware Object Sketching](https://clipasso.github.io/clipasso/)

--------------------------------------------
# Brain (NLP central)
## Memory
> My thinking: (this turns out to be exactly NTM) regard memory as a database. information generates key, query and value vectors. when new information comes, its query compares with key of all stored information. its value will be decoded and used as new query (thinking loop).  
### Storage
#### [NTM](https://arxiv.org/pdf/1410.5401.pdf)
- LSTM with external memory matrix. read and write memory like digital computer for each timestamp.
- What killed NTMs is that at the end of the day they're still recurrent networks, and thus inefficient and unstable to train in general.
- You don't need to have a external memory when you can apply attention to the whole input at once (sequential input is not really sequential when training).
- NTM as in program search is very interesting.
- Relationship with Transformer: ?

#### [Memory networks](https://arxiv.org/pdf/1410.3916.pdf)
concurrent with NTM but larger storage. tested mainly on question answering tests

#### [End-To-End Memory Networks](https://arxiv.org/pdf/1503.08895.pdf)
more with Memory networks

### Attention
#### [Neural machine translation by jointly learning to align and translate](https://arxiv.org/pdf/1409.0473.pdf)
Instead of decode from a fixed length encoding, keep all transformed embedding and selectively attend to those of interest. Intuition based.
