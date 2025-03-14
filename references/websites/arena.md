# Architecture
[transformer flowchart with parameter dimension](https://raw.githubusercontent.com/chloeli-15/ARENA_img/main/img/full-merm.svg)
## Tokenization
Byte-Pair encodings: " t", " a", "he", "in", "re",... "abs", "the", ... "revol", "98345",...
BOS token: It can act as a "rest position" for attention heads. I gpt2 same as EOS

### Vocab construction
- Initial vocabulary: ['a', 'b', 'c', ..., 'z', ' ', - '.', ...]
- Suppose 't' and 'h' are the most frequent pair →Merge them into 'th'.
- New vocabulary: ['a', 'b', 'c', ..., 'z', ' ', '.- ', 'th', ...]
- Next, suppose 'th' and 'e' are frequent → Merge them into 'the'.
- New vocabulary: ['a', 'b', 'c', ..., 'z', ' ', '.', 'th', 'the', ...]

### Tokenizing string
is space a token? Yes. can a token be a substring of another token? Yes.  Explanation: The tokenizer processes text from left to right and always chooses the **longest possible token** from the vocabulary that matches the current substring


### Some tokenization annoyances

```py
print(reference_gpt2.to_str_tokens("Ralph"))
print(reference_gpt2.to_str_tokens(" Ralph"))
print(reference_gpt2.to_str_tokens(" ralph"))
print(reference_gpt2.to_str_tokens("ralph"))

['<|endoftext|>', 'R', 'alph']
['<|endoftext|>', ' Ralph']
['<|endoftext|>', ' r', 'alph']
['<|endoftext|>', 'ral', 'ph']
```

```py
print(reference_gpt2.to_str_tokens("56873+3184623=123456789-1000000000"))

['<|endoftext|>', '568', '73', '+', '318', '46', '23', '=', '123', '45', '67', '89', '-', '1', '000000', '000']
```

## Embedding
### tied embedding
- same W_E and W_U. 
- note that if have a orthonormal embedding matrix, you taken the one hot vector and get the embedding, multiply the embeeding with the transposed embedding and you'll get the same one hot vector. 
- If we assume the embedding maps similar tokens to dot close embeeddings, then the output should have high logit scores for tokens similar to the input, with the input itself being 1.
- it's problematic bc we want $W_EW_U$ to model bigram frequency and the product of the matrix should not be symmetric  (eg white should be followed by house but not other way  around). If the matrices are  the  same the product is symmetric.

## Layer Norm
The scale (⊙γ) & translate (+β) is just a linear map. LayerNorm is only applied immediately before another linear map(either the MLP, or the query/key/value linear maps in the attention head, or the unembedding WU). Linear compose linear = linear, so we can just fold this into a single effective linear layer and ignore it. fold_ln=True flag in from_pretrained does this for you.

## Positional Embedding
distance of a key to a query matters

We'll focus on learned, absolute positional embeddings. This means we learn a lookup table mapping the index of the position of each token to a residual stream vector, and add this to the embed.

## Sampling
### History
- greedy
- beam
- beam with n-gram penalty to avoid repetition 
- surprise is good (Ari paper) -> stochastic sampling
- temperature
- top-k
- top-p (nucleus) (Ari paper)

### Sampler Implementation
the sample method generates new tokens autoregressively, by repeatedly:

- Passing the current sequence of tokens through the model to get logits,
- Using some sampling technique to select a new token, i.e. sample_next_token(input_ids, logits, **kwargs),
- Appending this new token to the input sequence,
- Repeating the process until one of the termination criteria is met: either we generate max_tokens_generated new tokens, or we generate the end-of-sequence token (which we can access via self.tokenizer.eos_token_id).

### Temp
- $P = \exp(-\frac{E_i}{T})= \exp(\frac{z_i}{T}) $, z is logit. So adding temperature is just z / T.

### KV Caching
> b is batch_size, n is token count, d is dim_head, h is N_head
- Remember that casual masking masks out the upper right triangle (n-1, n-1) in attn pattern, so the output from attn will only need *new query* from the newly generated token (b, 1, d, h) multiplied by the *new key* appended to the *old keys*. This results in a new attn pattern row at the bottom of size (1, n). The row is multilied by the *new value* appended to the *old values* to form the new row representing this  new token in attn output. 

# ----------
# Inspection of general transformer
- You can index weights like W_Q directly from the model via e.g. `model.blocks[0].attn.W_Q` (which gives you the `[nheads, d_model, d_head]` query weights for all heads in layer 0).
- But an easier way is just to index with `model.W_Q`, which gives you the `[nlayers, nheads, d_model, d_head]`
- model.W_E (embedding), model.W_U (unembed), model.W_pos, model.W_in (MLP 0), model.W_out (MLP 2), model.b_Q 

## Activation Cache

```py
for activation_name, activation in cache.items():
    # Only print for first layer
    if ".0." in activation_name or "blocks" not in activation_name:
        print(f"{activation_name:30} {tuple(activation.shape)}") 
```


## circuit_vis
```py
attention_pattern = gpt2_cache["pattern", 0]
gpt2_str_tokens = gpt2_small.to_str_tokens(gpt2_text)

display(
    cv.attention.attention_patterns(
        tokens=gpt2_str_tokens,
        attention=attention_pattern,
        attention_head_names=[f"L0H{i}" for i in range(12)],
    )
)
```

finding k-sparse neurons in residual stream

```py
neuron_activations_for_all_layers = t.stack([
    gpt2_cache["post", layer] for layer in range(gpt2_small.cfg.n_layers)
], dim=1)
# shape = (seq_pos, layers, neurons)

cv.activations.text_neuron_activations(
    tokens=gpt2_str_tokens,
    activations=neuron_activations_for_all_layers
)
```

finding k-sparse neurons in residual stream cont.
```py
neuron_activations_for_all_layers_rearranged = utils.to_numpy(einops.rearrange(neuron_activations_for_all_layers, "seq layers neurons -> 1 layers seq neurons"))

cv.topk_tokens.topk_tokens(
    # Some weird indexing required here ¯\_(ツ)_/¯
    tokens=[gpt2_str_tokens],
    activations=neuron_activations_for_all_layers_rearranged,
    max_k=7,
    first_dimension_name="Layer",
    third_dimension_name="Neuron",
    first_dimension_labels=list(range(12))
)
```

## Toy Attention Only
> For induction head to form earlier, The positional embeddings are only added to key and query vector - i.e. we compute queries as Q = (resid + pos_embed) @ W_Q + b_Q and same for keys, but values as V = resid @ W_V + b_V. This means that the residual stream can't directly encode positional information

> no MLP layers, no LayerNorms, and no biases.

```py
cfg = HookedTransformerConfig(
    d_model=768,
    d_head=64,
    n_heads=12,
    n_layers=2,
    n_ctx=2048,
    d_vocab=50278,
    attention_dir="causal",
    attn_only=True,  # defaults to False
    tokenizer_name="EleutherAI/gpt-neox-20b",
    seed=398,
    use_attn_result=True,
    normalization_type=None,  # defaults to "LN", i.e. layernorm with weights & biases
    positional_embedding_type="shortformer",
)
```

## Induction Head
- **Induction heads develop fairly suddenly in a phase change** - from about 2B to 4B tokens we go from no induction heads to pretty well developed ones. This is a striking divergence from a 1L model see the comparison of in context learning performance curves curves for models with different layers and can be observed in much larger models (eg a 13B one)
- **Induction heads are K-composition**, meaning (use ab->a[b]) the first layer changes residual stream for first b st its key will unlock a's query and brings its own value in. 

[induction heads in various models](https://www.neelnanda.io/mosaic) (note that each grid is a head of a layer and are not necessarily square)

## Hooks
### Basic Example (model.run_with_hook)
> We primarily use 2 layer attn only toy model where 1.4 and 1.10 are 2 induction heads, 0.7 is previous token head
```py
def hook_function(
    attn_pattern: Float[Tensor, "batch heads seq_len seq_len"],
    hook: HookPoint
) -> TT["batch", "heads", "seq_len", "seq_len"]:

    # modify attn_pattern (can be inplace)
    return attn_pattern

loss = model.run_with_hooks(
    tokens,
    return_type="loss",
    fwd_hooks=[
        ('blocks.1.attn.hook_pattern', hook_function)
    ],
    reset_hooks_end=True
)

model.reset_hooks()

# name filter
pattern_hook_names_filter = lambda name: name.endswith("pattern")

fwd_hooks=[(pattern_hook_names_filter, induction_score_hook)]

# or
fwd_hooks=[(lambda name: name.endswith("pattern")), hook_function]

# list comprehension
induction_head_layers = [5, 6, 7]
fwd_hooks = [
    (utils.get_act_name("pattern", induction_head_layer), visualize_pattern_hook)
    for induction_head_layer in induction_head_layers
]

# utils.get_act_name('pattern', 0) == 'blocks.0.attn.hook_pattern'


# use partial to pass more arguments to hook
# See Ablation section for usage example
def hook_with_extra_para(activation, hook, dumb_para):
    return activation[dumb_para]


model.run_with_hook(tokens, fwd_hooks=[(_, functools.partial(hook_with_extra_para, 0))])


# implementation of hook
class HookPoint(nn.Module):
    ...
    def forward(self, x):
        return x
    def layer() -> Int
```

### Direct Logit attribution
- For our toy model, `logits = (embed @ W_U) + (attn_out @ W_U) + (attn_out_1 @ W_U)`. 
- We use the example of last token "Harry" and see how it gives "Potter" after seeing "Harry Potter" before. Recall that W_U is (d_model, N_vocab) so we can think of the logit as key-lock match, where each column of W_U is a lock, and the residual stream for each token is a key. 
- To investigate why our last token produces high logit for "Potter", we only need to look at the  "Potter" lock. So `logit_Potter =  (embed @ W_U_Potter) + (attn_out @ W_U_Potter) + (attn_out_1 @ W_U_Potter)` which is a number. 
- We see that because **residual mechanism is additive**, the final logit contribution is a linear combination of every block's output dot W_U. 
> Note that with layer norm, DLA is no longer linear, but can be be seen as a local linear approx.

```py
def logit_attribution(
    embed: Float[Tensor, "seq d_model"],
    l1_results: Float[Tensor, "seq nheads d_model"],
    l2_results: Float[Tensor, "seq nheads d_model"],
    W_U: Float[Tensor, "d_model d_vocab"],
    tokens: Int[Tensor, "seq"],
) -> Float[Tensor, "seq-1 n_components"]:
    
    W_U_correct_tokens = W_U[:, tokens[1:]]

    direct_attributions = einops.einsum(W_U_correct_tokens, embed[:-1], "emb seq, seq emb -> seq")
    l1_attributions = einops.einsum(W_U_correct_tokens, l1_results[:-1], "emb seq, seq nhead emb -> seq nhead")
    l2_attributions = einops.einsum(W_U_correct_tokens, l2_results[:-1], "emb seq, seq nhead emb -> seq nhead")
    return t.concat([direct_attributions.unsqueeze(-1), l1_attributions, l2_attributions], dim=-1)
```
![](/images/arena-direct-logit-0.png)
![](/images/arena-direct-logit-rep.png)
> Each block represent direct contribution of the activation at the position to the logit of the correct next token. For example, the direct path represents bigram stats so the embedding of "manip" directly positively affect output of "ulative". Note that the first figure has positions going bottom to top and reversed for bottom figure.

> Note that this is stronger evidence that induction heads actually contributes to model power because just observing head as we studied the attn pattern doesn't mean it's necessarily using that information to make a concrete or correct prediction

### Ablation (Casual)
[types of ablation](https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J)

[zero ablation](https://arena-chapter1-transformer-interp.streamlit.app/[1.2]_Intro_to_Mech_Interp#exercise-induction-head-ablation)
```py
def head_zero_ablation_hook(
    z: Float[Tensor, "batch seq n_heads d_head"],
    hook: HookPoint,
    head_index_to_ablate: int,
) -> None:
    z[:, :, head_index_to_ablate, :] = 0.0

seq_len = (tokens.shape[1] - 1) // 2
logits = model(tokens, return_type="logits")
loss_no_ablation = -get_log_probs(logits, tokens)[:, -(seq_len - 1) :].mean()

for layer in tqdm(range(model.cfg.n_layers)):
    for head in range(model.cfg.n_heads):
        # Use functools.partial to create a temporary hook function with the head number fixed
        temp_hook_fn = functools.partial(head_zero_ablation_hook, head_index_to_ablate=head)
        # Run the model with the ablation hook
        ablated_logits = model.run_with_hooks(tokens, fwd_hooks=[(utils.get_act_name("z", layer), temp_hook_fn)])
        # Calculate the loss difference (= negative correct logprobs), only on the last `seq_len` tokens
        loss = -get_log_probs(ablated_logits.log_softmax(-1), tokens)[:, -(seq_len - 1) :].mean()
        ablation_scores[layer, head] = loss - loss_no_ablation
```
- ![](/images/arena-zero-ablation.png)

mean ablation
-  zero-ablation takes a model out of its normal distribution, and so the results from it aren't necessarily representative of what you'd get if you "switched off" the effect from some particular component.
- ![](/images/arena-mean-ablation.png)

> Note that 0.7 was not shown as a strong contributor in direct logit analysis. We can assume that this is because there are composition at layer 1 that used information indirectly from 0.7. 

## Induction Circuit Analysis
> We still use the toy model where 0.7 is previous token head and 1.4 and 1.10 are induction heads.

> There are 2 ways to do circuit analysis. One is to prepare some samples that you believe is processed by a certain circuit (like IOI) and verify its activations (eg, check its attn pattern output). Another is to directly analyze weights without running the model. We use both here (direct weight for copy and previous token head, input activation for circuit composition determination)
> 
> The way to analyze circuit is in the distill transformer circuit post. Basically the 2 keys are **additive residual pathway and KV OV decomposition of attention**.

How induction circuit works:
- The **previous token head** is a QK head and depends only on positional encoding (recall that our toy model adds pos emb only to K and Q input). Basically, if we take $pos^TW_{QK}pos$, this will be a off by 1 diagonal matrix. The effect of pos will be strong enough for us to ignore the actual token contributions
- The **copy head** is an OV head that copies the input embedding directly. It's diagonal. There are 2 heads that work together (1.4 and 1.10) to produce this diagonality. ![](/images/arena-2-vo.png)
```py
W_O_both = einops.rearrange(model.W_O[1, [4, 10]], "head d_head d_model -> (head d_head) d_model")
W_V_both = einops.rearrange(model.W_V[1, [4, 10]], "head d_model d_head -> d_model (head d_head)")

W_OV_eff = W_E @ FactoredMatrix(W_V_both, W_O_both) @ W_U

print(f"Fraction of the time that the best logit is on the diagonal: {top_1_acc(W_OV_eff):.4f}")
```

### Factorized Matrix Class
```py
head_index = 4
layer = 1

W_O = model.W_O[layer, head_index]
W_V = model.W_V[layer, head_index]
W_E = model.W_E
W_U = model.W_U

OV_circuit = FactoredMatrix(W_V, W_O)
full_OV_circuit = W_E @ OV_circuit @ W_U

OV_circuit.AB # the big unfactorized matrix
OV_circuit.norm()
OV_circuit.eigenvalues
OV_circuit.S # singular values in svd
OV_circuit.svd()  # returns 3 matrices of shape (m, r), (r,), (n, r) if input is (m,n)

```

### K-composition circuit
- the input to the second layer has contribution from 14 components (12 heads + original embedding + pos, recall toy model doesn't have MLP)
- by analyzing norm of inputs to 1.4 and 1.10's query and key from the 14 components, we see that the induction head/copy head uses query from embedding and key from layer 0 7th head.
![](/images/arena-induction-head-contri-to-q.png)
![](/images/arena-induction-head-contri-to-k.png)
- the attention pattern can also be decomposed to 14*14=196 elements (recall that W_QK is bilinear which means $(x_1+x_2)W_{QK}(y_1+y_2)=x_1W_{QK}(y_1+y_2)+x_2W_{QK}(y_1+y_2)=x_1W_{QK}y_1+x_1W_{QK}y_2+x_2W_{QK}y_1+x_2W_{QK}y_2$ for any tokens x and y, so each attention score can be linearly decomposed into 196 scores). We can guess that the most significant attention comes from head 0.7 and embedding and we can plot this particular pair's contribution to attention. Other attentions are much weaker.
![](/images/arena-induction-head-contri-to-attn.png)
- It's also possible to find a metric for each pair's contribution so we can plot the 14 by 14 contributions directly and see which pair has highest contribution. We use std.

# ----------
# Superposition
```py
t.manual_seed(2)

W = t.randn(2, 5)
W_normed = W / W.norm(dim=0, keepdim=True)

imshow(
    W_normed.T @ W_normed,
    title="Cosine similarities of each pair of 2D feature embeddings",
    width=600,
)

utils.plot_features_in_2d(
    W_normed.unsqueeze(0),  # shape [instances=1 d_hidden=2 features=5]
)
```

## Representing More Features than model dimensions
```py
utils.plot_features_in_2d(
      model.W,
      colors=model.importance,
      title=f"Superposition: {cfg.n_features} features represented in 2D space",
      subplot_titles=[f"1 - S = {i:.3f}" for i in feature_probability.squeeze()],
  )
```
![](/images/arena-superposition.png)
![](/images/arena-suepr-hidden.png)
Note that the generate batch function also uniform randomly select feature values from 0 to 1 so in first plot from left the whole square is filled since W=[[10000][01000]] and x = [11111] to [00000]. In the sparse regime, hidden states rarely fall outside of the feature directions. 
![](/images/arena-super-34510.png)
light color means higher importance

### (Anti)corelation
We could guess that superposition is even more common when features are anticorrelated (for a similar reason as why it's more common when features are sparse). Most real-world features are anticorrelated


### Privileged Basis
```py
def forward(self, features: Float[Tensor, "... inst feats"]) -> Float[Tensor, "... inst feats"]:
    activations = F.relu(
        einops.einsum(features, self.W, "... inst feats, inst d_hidden feats -> ... inst d_hidden")
    )
    out = F.relu(
        einops.einsum(activations, self.W, "... inst d_hidden, inst d_hidden feats -> ... inst feats")
        + self.b_final
    )
    return out
```
![](/images/arena-pb-2.png)
![](/images/arena-pb-345.png)

### Double Descent: Datapoint to Feature
- Initially, the model learns a memorising solution where datapoints are represented in superposition. This doesn't generalize, so we get low training loss but high test loss. 
> Consider the case of a language model which verbatim memorizes text. How can it do this? One naive idea is that it might use neurons to create a lookup table mapping sequences to arbitrary continuations. For every sequence of tokens it wishes to memorize, it could dedicate one neuron to detecting that sequence, and then implement arbitrary behavior when it fires. The problem with this approach is that it's extremely inefficient – but it seems like a perfect candidate for superposition, since each case is mutually exclusive and can't interfere.
- Later, the model learns a generalizing solution where features are learned and represented in superposition. This generalizes, so we get low training loss and low test loss.
- The spike in loss between these two happens when the model transitions between the memorising and generalizing solutions.

We'll use the toy model, but we'll train it by generating a random batch of data, and then using that *same batch for the entire training process*. We'll see **what happens when the batch sizes change**. According to our theory, the model should represent datapoints in superposition when the batch size is smaller than the number of features, and it should represent features in superposition when the batch size is larger than the number of features.

Dimensionality formula: $D_i = \frac{1}{\sum_j (x_i \cdot x_j)^2}$

![](/images/arena-mem-to-feature.png)
- hidden vectors mean the activations (h) or Wx. We are compressing 1000 features to 2 dimensions and varying number of training size (recall we use the same batch over steps). 
- If we look at the dataset  size=5 features and hidden, first features has 1000 points since there are 1000 columns in W, then hidden has 5 points since dataset has 5 samples. The hidden dimension here is 0.4 for all 5 samples because cos^2(72 degree) is 0.65, cos^2(144 degree) is 0.1 so sum is 2.5. 1/2.5=0.4.
- We continue to the right, adding samples. The hidden vectors are created as Wx. When sample size is small, x is basically one hot, and W just needs to store N_sample unique columns, and Wx just selects one of the columns as activation/embedding. This also results in the same shape of feature and activations.
- The phase transition happens around when sample size is equal to feature dim (it's a little earlier because of non 0 prob of more than 1 features appearing in one x). 
- Need to understand why N_sample>N_feature will cause this. Potentially related to deeper biological feature of learning.

# ----------
# Sparse Autoencoders (SAE)
> Models might have features/neurons responding to both Shakespear and gym (call it polysemantic, note it may not necessarily be superimposed). If this is all information we have regarding Shakespear/gym in the model, then there's nothing we can do to separate them. However, there are other neurons carrying other information that could be combined to precisely decide if the feature is Shakespear or gym. We could imagine a layer of 2-d where one is our polysemantic neuron and the other is another polysemantic neuron but react differently to Shakespear or gym. So in the 2-d activation space of this layer, we have 2 non-orthogonal but distinct directions. The SAE then just needs to copy the 2 directions in its rows so egg maximize one row and Shakespear another. 
 
## Thoughts
> Feature and human concept, privileged basis and polysematic neurons: The "polysemantic" neuron are polysemantic because of a mismatch between what features humans vs model uses. With this understanding, we say polysemantic neuron is any neuron that uses non human feature basis. Superposition implies polysemantism but the reverse is not true.

### Coding
we could encode 16 items on 16 bits or just 4 bits. What's the difference?  Now if we can decompose the items to independent components, say 2 by 8, then we can use 10 bits. But we can see the 4 bits case is just the asymptotic case where every possible binary dimension is independent (?).

If there are 4 features of an input, we could choose to encode in < 4 dimensions as explored in toy paper. Not much could be said for 4 dimensions encoding. But if we do > 4 dimensions, then we are effectively doing the 2^4=16 thing in reverse. The benefit is that, if we take these 4 features as just inputs with no corresponding human concept, then the features are hidden in the code, and we hope to find some features by iterating through all possible features. (This is like induction in that humans take complex inputs, lay them out one by one and try to infer some principle of the things that generated them)

### Dictionary Learning
Overcomplete basis 

## Toy Model (W^TWx) Autoencoding
### Architecture
- hidden: $h = Wx$
- latent: $z = relu(W_{enc }(h-b_{dec})+b_{enc})$
- reconstructed hidden: $h'=W_{dec}z+b_{dec}$
- goal of our SAE is to write the input as a linear combination of W_dec vectors
- encoder weight is (d_sae/n_feat, d_hidden/d_in) and decoder is (d_hidden/d_in, d_sae/n_feat), d_in means input to our SAE module.

For training toySAE, we use trained toy model (x'=W^TWx) and freeze weights. We train on reconstruction loss btw h and h' and sparsity loss of z.

what's importance?

### Weights and resampling to revive dead latent
visualization of encoder and decoder weight
![](/images/arena-sae-en-de.png)
Encoder is (5,2). We are seeing the rows as 2d vectors. The hidden activation is matched against the rows. This means the toy model W is the same as this W_enc. If we have feature (1,0000) then it's mapped to a direction by W and W_enc is just W^T. Decoder is W again. 

- As can be seen, there are dead latents/neurons which means some element of z will always be 0 (0 encoder weight dimension ). We resample these dead neurons and all weight graphs should be the perfect pentagon shape as in right side of above image. 

### Gating
Empirically, features usually seem to want to be binary. For instance, we often see features like "is this about a basketball" which are better thought of as "off" or "on" than occupying some continuous range from 0 to 1. 

### Capacity and reason behind all or none feature
https://arxiv.org/pdf/2210.01892.pdf

## Interpreting SAE Features
### SAELens
```py
gpt2 = HookedSAETransformer.from_pretrained("gpt2-small", device=device)
gpt2_sae, cfg_dict, sparsity = SAE.from_pretrained(
    release="gpt2-small-res-jb",
    sae_id="blocks.7.hook_resid_pre",
    device=str(device),
)


prompt = "Mitigating the risk of extinction from AI should be a global"
answer = " priority"

# --------------- compare model performance with and without sae layer method 1 ---------------
# without SAEs
test_prompt(prompt, answer, gpt2)

# with sae
with gpt2.saes(saes=[gpt2_sae]):
    test_prompt(prompt, answer, gpt2)

# with sae method 2
gpt2.add_sae(gpt2_sae)
test_prompt(prompt, answer, gpt2)
gpt2.reset_saes()  # Remember to always do this!

# with and without another method
logits = gpt2(prompt, return_type="logits")
top_prob, token_id_prediction = logits[0, -1].softmax(-1).max(-1)

logits_sae = gpt2.run_with_saes(prompt, saes=[gpt2_sae], return_type="logits")
top_prob_sae, token_id_prediction_sae = logits_sae[0, -1].softmax(-1).max(-1)

print(f"""Standard model: top prediction = {gpt2.to_string(token_id_prediction)!r}, prob = {top_prob.item():.2%}
SAE reconstruction: top prediction = {gpt2.to_string(token_id_prediction_sae)!r}, prob = {top_prob_sae.item():.2%}
""")

# --------------- get sae activation and check highest in neuronpedia ---------------
_, cache = gpt2.run_with_cache_with_saes(
    prompt,
    saes=[gpt2_sae],
    stop_at_layer=gpt2_sae.cfg.hook_layer + 1,
)
sae_acts_post = cache[f"{gpt2_sae.cfg.hook_name}.hook_sae_acts_post"][0, -1, :] # get final token
# {gpt2_sae.cfg.hook_name}.hook_sae_input     : (batch, n_tok, 768)
# {gpt2_sae.cfg.hook_name}.hook_sae_acts_pre  : (batch, n_tok, 24576) pre means pre-relu
# {gpt2_sae.cfg.hook_name}.hook_sae_acts_post : (batch, n_tok, 24576)
# {gpt2_sae.cfg.hook_name}.hook_sae_recons    : (batch, n_tok, 768)
# {gpt2_sae.cfg.hook_name}.hook_sae_output    : (batch, n_tok, 768)


# Plot line chart of latent activations
px.line(
    sae_acts_post.cpu().numpy(),
    title=f"Latent activations at the final token position ({sae_acts_post.nonzero().numel()} alive)",
    labels={"index": "Latent", "value": "Activation"},
    width=1000,
).update_layout(showlegend=False).show()

def display_dashboard(
    sae_release="gpt2-small-res-jb",
    sae_id="blocks.7.hook_resid_pre",
    latent_idx=0,
    width=800,
    height=600,
):
    release = get_pretrained_saes_directory()[sae_release]
    neuronpedia_id = release.neuronpedia_id[sae_id]

    # note the query contains neuronpedia_id which contains model and layer info and latent_idx
    url = f"https://neuronpedia.org/{neuronpedia_id}/{latent_idx}?embed=true&embedexplanation=true&embedplots=true&embedtest=true&height=300"

    print(url)
    display(IFrame(url, width=width, height=height))

# Print the top 5 latents, and inspect their dashboards
for act, ind in zip(*sae_acts_post.topk(3)):
    print(f"Latent {ind} had activation {act:.2f}")
    display_dashboard(latent_idx=ind)
```
> From the dashboard we see that the top 3 sae neurons are in charge of "global issues", "international contexts", and "legal and government terms"

### Neuronpedia Dashboard Impl (with ActivationStore)
```py
gpt2_act_store = ActivationsStore.from_sae(
    model=gpt2,
    sae=gpt2_sae,
    streaming=True,
    store_batch_size_prompts=16,
    n_batches_in_buffer=32,
    device=str(device),
)

tokens = gpt2_act_store.get_batch_tokens() # new batch everytime you call this
# tokens: (store_batch_size_prompts, 128) store_batch_size_prompts is number of sentences, 128 is number of tokens in one sentence

def show_activation_histogram(
    model: HookedSAETransformer,
    sae: SAE,
    act_store: ActivationsStore,
    latent_idx: int,
    total_batches: int = 10,
):
    sae_acts_post_hook_name = f"{sae.cfg.hook_name}.hook_sae_acts_post" # hook_name: 'blocks.7.hook_resid_pre'
    all_positive_acts = [] # simple list

    for i in tqdm(range(total_batches)):
        tokens = act_store.get_batch_tokens() # (16,128) 16 sentences each with 128 tokens
        _, cache = model.run_with_cache_with_saes(
            tokens, saes=[sae],
            stop_at_layer=sae.cfg.hook_layer + 1,
            names_filter=[sae_acts_post_hook_name],
        )
        acts = cache[sae_acts_post_hook_name][..., latent_idx]
        # cache[sae_acts_post_hook_name]: [16, 128, 24576]
        all_positive_acts.extend(acts[acts > 0].cpu().tolist())

    frac_active = len(all_positive_acts) / (total_batches * act_store.store_batch_size_prompts * act_store.context_size)

    px.histogram(
        all_positive_acts,
        nbins=50,
        title=f"ACTIVATIONS DENSITY {frac_active:.3%}",
        labels={"value": "Activation"},
        width=800,
        template="ggplot2",
        color_discrete_sequence=["darkorange"],
    ).update_layout(bargap=0.02, showlegend=False).show()

show_activation_histogram(gpt2, gpt2_sae, gpt2_act_store, latent_idx=9)
```

### Auto Interpretation
https://openai.com/index/language-models-can-explain-neurons-in-language-models/
https://blog.eleuther.ai/autointerp/

### Attn SAE or Direct Feature/Latent Attribution
Find tokens that activate attn sae the most
- run some inputs and collect activations at desired index [batch seq]
- get highest activating indices, use the indices to get both high activation values and tokens that correspond to this high activating latent
- get V [batch, seq, n_head, d] for high activating batches [k seq, n_head, d]
- get attn pattern [batch, n_head, seqQ, seqK] for high activating batches and high source/query locations [k, n_head, k, seqK]

### attn DLA and name mover feature
> sae features are trained on sparisity of data (feature as a property of the dataset st only a small fraction of data activates the feature)

steps (IOI task):
- find mary and john's W_U column, diff is called logit_direction
- collect attn sae cache at a layer and last token
- dot sae W_dec and W_O and the logit_direction

### 0 Ablation
```py
def logits_to_ave_logit_diff(
    logits: Float[Tensor, "batch seq d_vocab"],
    correct_toks: list[int] = correct_toks,
    incorrect_toks: list[int] = incorrect_toks,
    reduction: Literal["mean", "sum"] | None = "mean",
    keep_as_tensor: bool = False,
) -> list[float] | float

layer = 3
s2_pos = 10
assert gpt2.to_str_tokens(prompts[0])[s2_pos] == " John"


def ablate_sae_latent(
    sae_acts: Tensor,
    hook: HookPoint,
    latent_idx: int | None = None,
    seq_pos: int | None = None,
) -> Tensor:
    """
    Ablate a particular latent at a particular sequence position. If either argument is None, we ablate at all latents
    / sequence positions.
    """
    sae_acts[:, seq_pos, latent_idx] = 0.0
    return sae_acts


_, cache = gpt2.run_with_cache_with_saes(prompts, saes=[attn_saes[layer]])
acts = cache[hook_sae_acts_post := f"{attn_saes[layer].cfg.hook_name}.hook_sae_acts_post"]

alive_latents = (acts[:, s2_pos] > 0.0).any(dim=0).nonzero().squeeze().tolist()
ablation_effects = t.zeros(attn_saes[layer].cfg.d_sae)

logits = gpt2.run_with_saes(prompts, saes=[attn_saes[layer]])
logit_diff = logits_to_ave_logit_diff(logits)

for i in tqdm(alive_latents, desc="Computing causal effects for ablating each latent"):
    logits_with_ablation = gpt2.run_with_hooks_with_saes(
        prompts,
        saes=[attn_saes[layer]],
        fwd_hooks=[(hook_sae_acts_post, partial(ablate_sae_latent, latent_idx=i, seq_pos=s2_pos))],
    )

    logit_diff_with_ablation = logits_to_ave_logit_diff(logits_with_ablation)
    ablation_effects[i] = logit_diff - logit_diff_with_ablation

px.line(
    ablation_effects.cpu().numpy(),
    title=f"Causal effects of latent ablation on logit diff ({len(alive_latents)} alive)",
    labels={"index": "Latent", "value": "Causal effect on logit diff"},
    template="ggplot2",
    width=1000,
).update_layout(showlegend=False).show()

# Print the top 5 latents, and inspect their dashboards
for value, ind in zip(*ablation_effects.topk(3)):
    print(f"#{ind} had mean act {acts[:, s2_pos, ind].mean():.2f}, causal effect {value:.2f}")
    display_dashboard(
        sae_release="gpt2-small-hook-z-kk",
        sae_id=f"blocks.{layer}.hook_z",
        latent_idx=int(ind),
    )
```

### [SAE Attribution patching](https://arena-chapter1-transformer-interp.streamlit.app/[1.3.2]_Interpretability_with_SAEs#exercise-compare-ablation-to-attribution-patching)
```py
def get_cache_fwd_and_bwd(
    model: HookedSAETransformer, saes: list[SAE], input, metric
) -> tuple[ActivationCache, ActivationCache]:
    filter_sae_acts = lambda name: "hook_sae_acts_post" in name

    cache_dict = {"fwd": {}, "bwd": {}}
    def cache_hook(act, hook, dir: Literal["fwd", "bwd"]):
        cache_dict[dir][hook.name] = act.detach()

    with model.saes(saes=saes):
        with model.hooks(
            fwd_hooks=[(filter_sae_acts, partial(cache_hook, dir="fwd"))],
            bwd_hooks=[(filter_sae_acts, partial(cache_hook, dir="bwd"))],
        ):
            # Forward pass fills the fwd cache, then backward pass fills the bwd cache
            metric(model(input)).backward()

    return (
        ActivationCache(cache_dict["fwd"], model),
        ActivationCache(cache_dict["bwd"], model),
    )


clean_logits = gpt2.run_with_saes(prompts, saes=[attn_saes[layer]])
clean_logit_diff = logits_to_ave_logit_diff(clean_logits)

t.set_grad_enabled(True)
clean_cache, clean_grad_cache = get_cache_fwd_and_bwd(
    gpt2,
    [attn_saes[layer]],
    prompts,
    lambda logits: logits_to_ave_logit_diff(logits, keep_as_tensor=True, reduction="sum"),
)
t.set_grad_enabled(False)

hook_sae_acts_post = f"{attn_saes[layer].cfg.hook_name}.hook_sae_acts_post"
clean_sae_acts_post = clean_cache[hook_sae_acts_post]
clean_grad_sae_acts_post = clean_grad_cache[hook_sae_acts_post]

# Compute attribution values for all features, then index to get live ones
attribution_values = (clean_grad_sae_acts_post * clean_sae_acts_post)[:, s2_pos, alive_features].mean(0)

# Visualize results
px.scatter(
    pd.DataFrame(
        {
            "Ablation": ablation_effects[alive_latents].cpu().numpy(),
            "Attribution Patching": attribution_values.cpu().numpy(),
            "Latent": alive_latents,
        }
    ),
    x="Ablation",
    y="Attribution Patching",
    hover_data=["Latent"],
    title="Attribution Patching vs Ablation",
    template="ggplot2",
    width=800,
    height=600,
).add_shape(
    type="line",
    x0=attribution_values.min(),
    x1=attribution_values.max(),
    y0=attribution_values.min(),
    y1=attribution_values.max(),
    line=dict(color="red", width=2, dash="dash"),
).show()
```

## SAE Circuits
We should expect that not only are individual latents generally sparse, they are also sparsely connected.

### Latent to Latent Gradient
```py
# Computed with no gradients, and not patching in SAE reconstructions...
layer_1_latents, layer_2_latents = model.run_with_cache_with_saes(...)

def latent_acts_to_later_latent_acts(layer_1_latents):
    layer_1_resid_acts_recon = SAE_1_decoder(layer_1_latents)
    layer_2_resid_acts_recon = model.blocks[layer_1: layer_2].forward(layer_1_resid_acts_recon)
    layer_2_latents_recon = SAE_2_encoder(layer_2_resid_acts_recon)
    return layer_2_latents_recon

latent_latent_gradients = torch.func.jacrev(latent_acts_to_later_latent_acts)(layer_1_latents) # Jacobian reverse-mode differentiation
```
> Note that we are using the sae latent computed from reconstruction of residual stream from eariler latent so this approach works better if your sae is good

A SparseTensor class is defined since latent size by latent size tensor is too big to fit in memory.

![](/images/arena-sae-latent-grad-03.png)
Many of the nonzero gradients are for pairs of tokens which fire on the same token. There aren't as many cross-token gradients. One of the most notable is (F0.16911, " E") -> (F3.15266, "iff") which seems like it could be a bigram circuit for words which start with " E"

`
display_dashboard(sae_id="blocks.0.hook_resid_pre", latent_idx=16911)
display_dashboard(sae_id="blocks.3.hook_resid_pre", latent_idx=15266)
`

### Token to Latent Gradient
```py
def tokens_to_latent_acts(
    token_scales: Float[Tensor, "batch seq"],
    tokens: Int[Tensor, "batch seq"],
    sae: SAE,
    model: HookedSAETransformer,
) -> tuple[Tensor, tuple[Tensor]]:
    """
    Given scale factors for model's embeddings (i.e. scale factors applied after we compute the sum
    of positional and token embeddings), returns the SAE's latents.
    """
    resid_after_embed = model(tokens, stop_at_layer=0)
    resid_after_embed = einops.einsum(resid_after_embed, token_scales, "... seq d_model, ... seq -> ... seq d_model")
    resid_before_sae = model(resid_after_embed, start_at_layer=0, stop_at_layer=sae.cfg.hook_layer)

    sae_latents = sae.encode(resid_before_sae)
    sae_latents = SparseTensor.from_dense(sae_latents)

    return sae_latents.sparse[0], (sae_latents.dense,)


def token_to_latent_gradients(
    tokens: Float[Tensor, "batch seq"],
    sae: SAE,
    model: HookedSAETransformer,
) -> tuple[Tensor, SparseTensor]:
    token_scales = t.ones(tokens.shape, device=model.cfg.device, requires_grad=True)
    token_latent_grads, (latent_acts_dense,) = t.func.jacrev(tokens_to_latent_acts, has_aux=True)(token_scales, tokens, sae, model)

    token_latent_grads = einops.rearrange(token_latent_grads, "d_sae_nonzero batch seq -> batch seq d_sae_nonzero")

    latent_acts = SparseTensor.from_dense(latent_acts_dense)

    return (token_latent_grads, latent_acts)
```
![](/images/arena-sae-token-latent-grad-03.png)
In the previous exercise, we saw gradients between (F0.16911, " E") -> (F3.15266, "iff"), which seems like it could be forming a bigram circuit for words which start with " E". In this plot, we can see a gradient between the " E" token and feature F3.15266, which is what we'd expect based on this.

### Latent to Logit Gradient
we can consider latents as having a dual nature: when looking back towards the input, they are representations, but when looking forward towards the logits, they are actions. (this is expected since latent are formed by noting the similarity in both inputs and outputs) We might expect sparsity in both directions, in other words not only should latents sparsely represent the activations produced by the input, they should also sparsely affect the gradients influencing the output.

![](/images/arena-sae-latent-logit-grad-03.png)
> Note that we choose top 25 logits on y axis. Latents taken at layer 9. The numbers in x axis after token is the token position, since each token have d_sae number of latents and all seq x d_sae latents contribute to final logit

We see that feature F9.22250 stands out as boosting the " Paris" token far more than any of the other top predictions. Investigation reveals this feature fires primarily on French language text, which makes sense! We also see F9.5879 which seems to strongly boost words associated with Germany (e.g. Berlin, Hamberg, Cologne, Zurich). We see a similar pattern there, where that feature mostly fires on German-language text (or more commonly, English-language text talking about Germany).

## Variants of SAE
### Transcoder
https://www.lesswrong.com/posts/YmkjnWtZGLbHRbzrP/transcoders-enable-fine-grained-interpretable-circuit
transcoders operate on activations both before and after an MLP sublayer: they take as input the pre-MLP activations, and then aim to represent the post-MLP activations of that MLP sublayer as a sparse linear combination of feature vectors.

Transcoders decompose the MLPs themselves into interpretable computations. In contrast, SAEs only allow us to interpret the output of MLP sublayers. SAEs don’t play nice with circuit discovery methods. they don’t tell us how this activation is computed in the first place.
  
> It's essentailly just MLP but with larger d_mlp and sparsity loss. 

Circuit:
- Fundamentally, when we approach circuit analysis with transcoders, we are asking ourselves which earlier-layer transcoder features are most important for causing a later-layer feature to activate
- input independent and input dependent analysis: feature to feature gradient is an operator so if you have input, it gives a vector of activations on later transcoder layer from a specific input.

thoughts
- I wonder how a pure transcoder will perform  (in which case the only non-linearity comes from attn)
- siince this is a linear approx to a non linear MLP, i wonder how exactly does the sparsity constraint affect the transcoder. I imagine the recon loss will restrict the transcoder weight to a very narrow domain. 

### [Crosscoder](https://transformer-circuits.pub/2024/crosscoders/index.html)



# ----------
# IOI



# ----------
# Function Vector
nnsignt API key: 9ef93dff0ad54437bdc5dde55a9394b6

### [nnsight](https://nnsight.net/notebooks/tutorials/walkthrough)
basic intervention
```py
with tiny_model.trace(input):

    # Save the output before the edit to compare.
    # Notice we apply .clone() before saving as the setting operation is in-place.
    l1_output_before = tiny_model.layer1.output.clone().save()

    # Access the 0th index of the hidden state dimension and set it to 0.
    tiny_model.layer1.output[:, 0] = 0

    # Save the output after to see our edit.
    l1_output_after = tiny_model.layer1.output.save()

print("Before:", l1_output_before)
print("After:", l1_output_after)
```
tokenizer

trace
```py
REMOTE = True
CONFIG.set_default_api_key("9ef93dff0ad54437bdc5dde55a9394b6")

prompt = "The Eiffel Tower is in the city of"

with model.trace(prompt, remote=REMOTE):
    # h (hidden) is a list of modules
    hidden_states = model.transformer.h[-1].output[0].save()

    # Save the model's logit output
    logits = model.lm_head.output[0, -1].save()

# Get the model's logit output, and it's next token prediction
print(f"logits.shape = {logits.value.shape} = (vocab_size,)")
print("Predicted token ID =", predicted_token_id := logits.value.argmax().item())
print(f"Predicted token = {tokenizer.decode(predicted_token_id)!r}")

# Print the shape of the model's residual stream
print(f"\nresid.shape = {hidden_states.value.shape} = (batch_size, seq_len, d_model)")
```

batching
```py
with llm.trace() as tracer:

    with tracer.invoke("The Eiffel Tower is in the city of"):

        # Ablate the last MLP for only this batch.
        llm.transformer.h[-1].mlp.output[0][:] = 0

        # Get the output for only the intervened on batch.
        token_ids_intervention = llm.lm_head.output.argmax(dim=-1).save()

    with tracer.invoke("The Eiffel Tower is in the city of"):

        # Get the output for only the original batch.
        token_ids_original = llm.lm_head.output.argmax(dim=-1).save()


print("Original token IDs:", token_ids_original)
print("Modified token IDs:", token_ids_intervention)

print("Original prediction:", llm.tokenizer.decode(token_ids_original[0][-1]))
print("Modified prediction:", llm.tokenizer.decode(token_ids_intervention[0][-1]))

# Original token IDs: tensor([[ 198,   12,  417, 8765,  318,  257,  262, 3504, 7372, 6342]],
#        device='mps:0')
# Modified token IDs: tensor([[ 262,   12,  417, 8765,   11,  257,  262, 3504,  338, 3576]],
#        device='mps:0')
# Original prediction:  Paris
# Modified prediction:  London
```

### Function Vector
ROME based activation patching and find attention heads by measuring causal indirect effect of last token attn activations. Difference is that they take highest average indirect effect heads' output across samples for a task and add it to another task. This has better result than using average mlp activation of a task across samples 






# Library
## Python Basics
### Type annotation
> typing doesn't affect runtime behavior
```py
from typing import Union, List, Dict, Optional, Tuple

Vector = List[float]

def divide(a: float, b: float) -> Union[Vector, str]:
    if b == 0:
        return "Error: Division by zero"
    return [a, b, a / b]
```

### decorators
Decorator pattern
- Decorator use can be more efficient than subclassing, because an object's behavior can be augmented without defining an entirely new object.

Mechanism
- https://stackoverflow.com/questions/739654/how-do-i-make-function-decorators-and-chain-them-together/1594484#1594484
- a decorator takes a function and returns a "decorated" function
```py
decorator(func):
    def decorated_func(foo):
        print("I'm decorated"+foo)
        return func(foo)
    return decorated_func()

@decorator
def now_i_am_decorated(foo):
    return foo

now_i_am_decorated()

### ------ method decorator ------ 
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # The wrapper accepts any arguments
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Do I have args?:")
        print(args)
        print(kwargs)

        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")

function_with_no_argument()
#outputs
#Do I have args?:
#()
#{}
#Python is cool, no argument here.

class Mary(object):
    def __init__(self):
        self.age = 31
    
    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3): # You can now add a default value
        print("I am {0}, what did you think?".format(self.age + lie))

m = Mary()
m.sayYourAge()
#outputs
# Do I have args?:
#(<__main__.Mary object at 0xb7d303ac>,)
#{}
#I am 28, what did you think?

### ------ decorator with argument ------ 
def repeat(num_times):
    """
    A decorator that repeats the execution of the decorated function
    a specified number of times.
    """
    # This is the actual decorator that will be applied to the function.
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    # Return the decorator function.
    return decorator_repeat

# Using the decorator with an argument.
@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```


Auto-generated methods: __init__, __repr__, __eq__, and __hash__

```py
class Circle:
    def __init__(self, radius):
        self._radius = radius  # "Private" variable

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14 * self._radius ** 2  # Computed property

circle = Circle(5)
print(circle.radius)  # Output: 5 (uses the getter)
circle.radius = 10    # Uses the setter (validates input)
print(circle.area)    # Output: 314.0 (computed dynamically)
```

### rich
The `rich` library is a helpful little library to display outputs more clearly in a Python notebook or terminal. It's not necessary for this workshop, but it's a nice little tool to have in your toolbox.

The most important function is `rich.print` (usually imported as `rprint`). This can print basic strings, but it also supports the following syntax for printing colors:

```python
rprint("[green]This is green text[/], this is default color")
```

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/rprint-1.png" width="350">

and for making text bold / underlined:

```python
rprint("[u dark_orange]This is underlined[/], and [b cyan]this is bold[/].")
```

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/rprint-2.png" width="350">

It can also print tables:

```python
from rich.table import Table

table = Table("Col1", "Col2", title="Title") # title is optional
table.add_row("A", "a")
table.add_row("B", "b")

rprint(table)
```

<img src="https://raw.githubusercontent.com/info-arena/ARENA_img/main/misc/rprint-3.png" width="150">

The text formatting (bold, underlined, colors, etc) is also supported within table cells.


### class functions
- __repr__: str()

## Example Codes
### Memory management
```py
import part31_superposition_and_saes.utils as utils

# Profile memory usage, and delete gemma models if we've loaded them in
namespace = globals().copy() | locals()
utils.profile_pytorch_memory(namespace=namespace, filter_device="cuda:0")

del gemma_2_2b
del gemma_2_2b_sae

THRESHOLD = 0.1  # GB
for obj in gc.get_objects():
    try:
        if isinstance(obj, t.nn.Module) and part32_utils.get_tensors_size(obj) / 1024**3 > THRESHOLD:
            if hasattr(obj, "cuda"):
                obj.cpu()
            if hasattr(obj, "reset"):
                obj.reset()
    except:
        pass

# Move our gpt2 model & SAEs back to GPU (we'll need them for the exercises we're about to do)
gpt2.to(device)
gpt2_saes = {layer: sae.to(device) for layer, sae in gpt2_saes.items()}

part32_utils.print_memory_status()
```

### Creation
- HookedTransformer = HookedTransformer.from_pretrained("gpt2-small")
- HookedTransformer.from_config(cfg)
- `reference_gpt2 = HookedTransformer.from_pretrained(
    "gpt2-small",
    fold_ln=False,
    center_unembed=False,
    center_writing_weights=False
)`


### Tokenization
- `sorted_vocab = sorted(list(reference_gpt2.tokenizer.vocab.items()), key=lambda n: n[1])`
- `reference_gpt2.to_str_tokens("Ralph")     #['<|endoftext|>', 'R', 'alph']`
- `reference_gpt2.to_tokens("Ralph")     #tensor([[50256,    49, 17307]], device='cuda:0')`
-  `next_token = logits[0, -1].argmax(dim=-1)
    next_char = reference_gpt2.to_string(next_token)`


### Inference
- logits, cache = reference_gpt2.run_with_cache(tokens)




## Structure
### transformer_lens 
- class HookedTransformer
    - var tokenizer
        - prop vocab 
        - func batch_decode(tensor)
    - func to_str_tokens(str) -> list(str)
    - func to_tokens(str) -> tensor
    - func to_string(tensor) -> string
    - func named_parameters() -> list[(str, Parameter)]

    - func run_with_cache(tensor) -> logits, cache:ActivationCache

- class ActivationCache
    - `func __getitem__(self, key) -> torch.Tensor[Usually of shape (batch seq d)]`: 
        ``` py   
        ('k', 6, 'a')=='blocks.6.attn.hook_k'
        ('pre', 2)=='blocks.2.mlp.hook_pre'
        ('embed')=='hook_embed'
        ('normalized', 27, 'ln2')=='blocks.27.ln2.hook_normalized'
        ('k6')=='blocks.6.attn.hook_k'
        ('scale4ln1')=='blocks.4.ln1.hook_scale'
        ('pre5')=='blocks.5.mlp.hook_pre'

        act_name_alias = {
            "attn": "pattern",
            "attn_logits": "attn_scores",
            "key": "k",
            "query": "q",
            "value": "v",
            "mlp_pre": "pre",
            "mlp_mid": "mid",
            "mlp_post": "post",
        }
        ```

- utils 
    - func gelu_new 
    - func tokenize_and_concatenate
    - test_prompt(prompt, answer, model)

- class Config
    - n_layers 
    - n_heads 
    - n_ctx # context window




### transformers
- models
    - gpt2
        - tokenization_gpt2_fast
            - class GPT2TokenizerFast
### circuitsvis
- attention
    - func attention_patterns(tokens, attn)

### sae_lens
- toolkit
    - pretrained_saes_directory
        - pretrained_saes_directory()
- SAE
    - var cfg
        - d_sae, d_in, hook_name, hook_layer,neuronpedia_id
    - W_enc
    - W_dec
    - from_pretrained(release:str,sae_id:str,device)->sae:SAE, cfg_dict, sparsity
    
    
- ActivationsStore

- HookedSAETransformer
    - from_pretrained(model_name: str, device)
    - run_with_saes(prompt, saes:[SAE], return_type="logits")
    - run_with_cache_with_saes(prompt, saes:[SAE],stop_at_layer:int)->None,cache:ActivationCache
    - with saes(saes:[SAE])
    - add_sae(sae:SAE)
    - reset_saes()
- LanguageModelSAERunnerConfig

### sae_vis

### nnsight
- LanguageModel
```css
LlamaForCausalLM(
  (model): LlamaModel(
    (embed_tokens): Embedding(128256, 4096)
    (layers): ModuleList(
      (0-31): 32 x LlamaDecoderLayer(
        (self_attn): LlamaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
        )
        (mlp): LlamaMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): LlamaRMSNorm((4096,), eps=1e-05)
        (post_attention_layernorm): LlamaRMSNorm((4096,), eps=1e-05)
      )
    )
    (norm): LlamaRMSNorm((4096,), eps=1e-05)
    (rotary_emb): LlamaRotaryEmbedding()
  )
  (lm_head): Linear(in_features=4096, out_features=128256, bias=False)
  (generator): Generator(
    (streamer): Streamer()
  )
)

GPTJForCausalLM(
  (transformer): GPTJModel(
    (wte): Embedding(50400, 4096)
    (drop): Dropout(p=0.0, inplace=False)
    (h): ModuleList(
      (0-27): 28 x GPTJBlock(
        (ln_1): LayerNorm((4096,), eps=1e-05, elementwise_affine=True)
        (attn): GPTJAttention(
          (attn_dropout): Dropout(p=0.0, inplace=False)
          (resid_dropout): Dropout(p=0.0, inplace=False)
          (k_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (v_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (out_proj): Linear(in_features=4096, out_features=4096, bias=False)
        )
        (mlp): GPTJMLP(
          (fc_in): Linear(in_features=4096, out_features=16384, bias=True)
          (fc_out): Linear(in_features=16384, out_features=4096, bias=True)
          (act): NewGELUActivation()
          (dropout): Dropout(p=0.0, inplace=False)
        )
      )
    )
    (ln_f): LayerNorm((4096,), eps=1e-05, elementwise_affine=True)
  )
  (lm_head): Linear(in_features=4096, out_features=50400, bias=True)
  (generator): Generator(
    (streamer): Streamer()
  )
)
```
### Torch
- class tensor
    - func softmax(dim)
    - func argmax(dim)
    - func masked_fill_(mask, value)
    - func masked_fill(mask, value)->tensor
    - func bool()

- func ones/zeros/eye
- func cat([])
- func triu(size, N_shift_up) # lower is 0
- nn 
    - functional
        - func normalize(tensor, p (Lp norm), dim)
    - module
        - func registerBuffer(name, value, dtype, device)
        - func load_state_dict(state_dict)
        - func state_dict()

### Broadcasting
1. right to left
2. if last dimension of one tensor matches any dimension of the other
    - (a, b, c), (c): c should not be followed by anything, nor preceded by anything other than 1 or (a, b) or b
3. if no match, check if there's trailing 1, if yes, remove and do 2 again

### Einstein sum
$S=\text{einops.einsum} (A, B, a_0\ a_1\ a_2\ \dots, b_0\ b_1\ b_2\ \dots -> \{a_0, b_0, \phi\} \{a_1, b_1, \phi\} \dots)$. This means, if we want to keep a_0 and b_0 (which means a_i need to have same dimension as b_i), $S_{ia_0, ib_0}:=S[ia_0, ib_0]=\sum_{i_1, i_2, \dots}A[ia_0, i_1, i_2, \dots]B[ib_0, i_1, i_2, \dots]$

- 'abc,abd->cd', 'abc,dbe->eacd', ie, $\text{output}_{e,a,c,d} = \sum_{b} \text{tensor1}_{a,b,c} \cdot \text{tensor2}_{d,b,e}$
- 'qnd,knd->nqk' This means $\text{output}_{n,q,k} = \sum_{d} \text{tensor1}_{q,n,d} \cdot \text{tensor2}_{k,n,d}$
- 'abc,abc->abc': element wise product
- 'ab,bc->ac': matrix product
- 'a,b->ab': outer product