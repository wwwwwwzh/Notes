# Summary
OPENAI
- gpt 2: 1.5b parameters, decoder only, next token objective
- gpt 3: 175b parameters
- gpt 3.5/instruct: optional SFT with RLHF ![](/images/rlhf.png)
- gpt 4: multimodal, 25,000 tokens context, SFT for cot
- gpt 4o
- gpt o1 preview
- gpt o1: possibly rewarding longer cot, [possible inference time hacks](https://zhuanlan.zhihu.com/p/773907223)

DEEPSEEK
- deepseek v1 (scaling law): 67b, 2t training tokens, LLaMA architecture, high quality data, SFT, DPO for alignment. Comprehensive scaling law research (batchsize and lr, data and model scale) 
- deepseekmath (GRPO)
- deepseekmoe
- deepseek v2 (economical): 236b (21b activated for each token), 8t training tokens, 128k context length, Multi-head Latent Attention (**MLA**) and **DeepSeekMoE**. SFT, **GRPO**.
- deepseek v3: 671b/37b, 15t, 2.8m gpu hours, auxiliary-loss-free strategy for load balancing and multi-token prediction training objective.
- deepseek r1-zero: V3 with pure GRPO RL and fixed reward rules, https://zhuanlan.zhihu.com/p/19843230707, aha moment, poor readability, and language mixing
- deepseek r1: cold start with SFT and zero style RL but with language consistency reward, save checkpoint and generate more SFT data (800k) to train another v3 base, RL again. qwen and llama distill (no RL just SFT) with the 800k generated data. section 4.2 includes unsuccessful attempts at developing this model

LLAMA

QWEN

OTHERS
- [DeepScaleR](https://huggingface.co/agentica-org/DeepScaleR-1.5B-Preview): RL on DeepSeek-R1-Distilled-Qwen-1.5B (this is SFT only). Reward is just right or wrong answer



# Tricks
## MOE
### Basic
https://cameronrwolfe.substack.com/p/moe-llms
- MLP layers are copied to create N "experts"
- routing using a network on the incoming token to decide which experts to use. The oriiginal moe uses a linear projection of the token to N-d vector followed by softmax.
- To encourage balance of training among experts, add a coefficient of variation loss on router's output prob distribution
- To encourage balance of number of tokens to each expert use a load balancing loss: ![](/images/moe-load-balancing.webp)
cons:
- Prone to instabilities during training.
- Difficult to finetune (i.e., due to issues with overfitting).
- Sensitive to low / mixed precision training techniques.
- Sensitive to hyperparameter settings (e.g., weight initialization).
## RL/Reasoning
https://zhuanlan.zhihu.com/p/773907223
- post training vs inference
- verifier guided inference
- sft
- search

### RLHF
reward model
- Process supervised (PRM): sample：a=5-2，b=a+1，b?<step1_start> a=5-2=3<step1_end> <step2_start> b=3+1=4<step2_end>
- Outcome supervised (ORM)

Pipeline
- we have pretrained LLM
- Train reward model: By comparing model outputs in head-to-head matchups, an Elo system can be used to generate a ranking of the models and outputs relative to each-other. These different methods of ranking are normalized into a scalar reward signal for training.
- At this point in the RLHF system, we have an **initial language model** that can be used to generate text and a **preference model** that takes in any text and assigns it a score
- Train LLM with reward: fine-tune some or all of the parameters of a copy of the initial LM with a policy-gradient RL algorithm, Proximal Policy Optimization (PPO). Some parameters of the LM are frozen because fine-tuning an entire 10B or 100B+ parameter model is prohibitively expensive (for more, see Low-Rank Adaptation (LoRA) for LMs or the Sparrow LM from DeepMind)
- PPO: First, **the policy is a language model** (copy of the initial LLM) that takes in a prompt and returns a sequence of text (or just probability distributions over text). The action space of this policy is all the tokens corresponding to the vocabulary of the language model (often on the order of 50k tokens) and the observation space is the distribution of possible input token sequences, which is also quite large given previous uses of RL (the dimension is approximately the size of vocabulary ^ length of the input token sequence). The reward function is a combination of the preference model and a constraint on policy shift.
![](/images/rlhf-2.png)

### Direct preference optimization (DPO)
https://zhuanlan.zhihu.com/p/721073733

no RL, implicit reward model. 

### GRPO 
https://zhuanlan.zhihu.com/p/20812786520
https://www.zhihu.com/question/10766825126/answer/88583863333

## Others
### LORA
Most problems use a small subspace of a model's parameter space, in other words, if we want to introduce a new task, we only need to refine a small subset of model parameter. In models like transformer, parameters are represented as matrices. Subspace of parameters are subspaces of the matrices. Therefore, to finetune a matrix (MLP or KVQ), we just add a low rank matrix represented as W'=AB where A and B have the same low rank (<=8, 1 works well). The output of the operator becomes h=(W+W')x=Wx+ABx. Thus, we can view the LORA module as a separate path in model. 




# Some Notes
- china kWh 7.8 cents, us 17 cents
training cost compare
- [v3-llama training compare](https://apxml.com/posts/training-cost-deepseek-v3-vs-llama-3): 
- gpt-3: 0.7m hours, V100
- v3: 3m gpu hours, 2048 H800
- llama 3: 30m gpu hours
- grok 3: 200m hours, 100k H100


## Answer from different models
### o1
Use option enter with ^ or ^. to select all start of line or start of non empty lines.

> The user is asking about technical implementations for GPT-2, GPT-3, GPT-3.5, GPT-4, GPT-4o, GPT-o1, and GPT-o3. I’ll start by summarizing key details like parameter count, architecture, training, and techniques.
> 
> I'll organize the information into bullet points. For instance:
> 
> GPT-2: Transformer-based, decoder-only model, with 1.5B parameters, pre-trained with unsupervised next-word prediction.
> 
> GPT-3: Scaling up to 175B parameters, follows the same transformer-based architecture but on a much larger scale.
> 
> I’ll ensure clarity and consistency in the rest of my answer too.
> 
> The user wants technical details. I’m breaking it down version by version:
> 
> GPT-3: Dense decoder architecture, sparse attention at scale. Uses training techniques like mixed precision, distributed training, and few-shot learning.
> 
> GPT-3.5: Fine-tuned GPT-3 with reinforcement learning (RLHF), optimized for better dialogue responses.
> 
> GPT-4: A multimodal model with an extended context window, RLHF, and improvements for reasoning and image handling.
> 
> GPT-4o: A variant of GPT-4 optimized for efficiency and multimodal input, possibly involves distillation or quantization.
> 
> GPT-o1 & GPT-o3: Focus on reasoning with explicit steps and advanced reinforcement learning techniques, improving efficiency and safety.

> The question is about "group query attention." I think it might refer to group relative policy optimization (GRPO) used in DeepSeek, but "group query attention" isn't a standard term in transformer literature. Let me check references. Our previous discussion mentioned GRPO and group queries. I’ve found that GRPO samples a group of outputs from the old policy, but that's not exactly “group query attention.” Still, “group query attention” could refer to a way of grouping queries within multi-head attention.
> 
> "Group query attention" might be a variant of multi-head attention where queries are grouped together to share computation. I think I’ve seen it mentioned in research aimed at reducing memory complexity. Papers like those on "Grouped Query Attention" in vision transformers often group queries in a structured way. It could also refer to techniques like sparse attention or methods like Linformer and BigBird that reduce computation. Essentially, group query attention aggregates query representations before attention, making computation more efficient in long sequences.

> The user asks about the "other side" of a right triangle with sides of length 2 and 3. This wording is a bit ambiguous since it's unclear if 2 and 3 are the legs or if one is the hypotenuse.
> 
> If we assume 2 and 3 are the legs, we can find the hypotenuse using the Pythagorean theorem: sqrt(2^2 + 3^2) = sqrt(4 + 9) = sqrt(13).
> 
> So, if that's the case, the other side is sqrt(13).
> 
> If 3 is the hypotenuse, then using the Pythagorean theorem, the other leg is sqrt(3^2 - 2^2) = sqrt(9 - 4) = sqrt(5). But if 2 were the hypotenuse, it wouldn't work since it's smaller than 3.
> 
> The question is ambiguous — it doesn't clearly tell if 2 and 3 are legs or if 3 is the hypotenuse. Typically, the longest side is assumed to be the hypotenuse, so it’s likely 3 is the hypotenuse.
> 
> But I might need a clarifying question to be sure.


# Inside the Model


### SAE
1. find latent feature of interest in neuronpedia or the custom max act function
2. use the latent to index sae decoder column and use that column as control vector on output of sae or original token stream

# MATS Appl
Some keywords:
- <think></think>
- Okay, 
- Let's see, 
- Let me think, 
- Okay, let me think about this.
- 嗯，这个问题看起来有点意思。让我仔细想想。
- 嗯，

- I remember
- First off, Next, Then, Lastly
- Right, so that's the key here.
- 首先，
- 另一个思路是

- Wait, ..., maybe
- But hold on, maybe
- No, that's not right.
- Hmm, I'm not sure.
- But maybe
- 不过这里可能需要更仔细地分析。
- 不过，
- 但是
- 不过再仔细想想，
- 或者
- 或者这样：

- Alternatively, 
- Hmm, perhaps
- Hmm, it seems like, .... maybe, 
- Perhaps, Also, Another
- So, perhaps
- Wait, I think I've reached the limit of my ability to solve this problem.

## Doc
executive summary and ideally contains a bunch of graphs, and enough detail to follow what you did without needing to read your code. Ideally also a Colab notebook with your results. Please prioritise making the google doc clear and easy to read (over making the code easy to read), and remember to let anyone with the link access the doc! 
### Executive Summary Format
The first 1-3 pages of the google doc should be an executive summary, which gives the broad strokes of what you did and what you learned. Something at ~1 page (including graphs) is great, max 3 pages and max 600 words. Please include key graphs!

One good format is to have sections for:
- What problem am I trying to solve? (and a bit on why you think it’s interesting)
- What are your high-level takeaways? What were the most interesting parts of your project?
- One paragraph and graph per key experiment, giving the gist of what it was, what you found, and why this supports your key takeaways


### Drafts
#### Executive summary
This is a preliminary investigation on why models fine tuned by deepseek-r1 data evolved reasoning ability. I use 2 models: Qwen2.5-Math-1.5B model (hereafter called original or qw/qwen) and DeepSeek-R1-Distill-Qwen-1.5B (hereafter r1 or ds/deepseek), since the later is a sft version of the former. 

It's observed that deepseek-r1 distilled models generally generate longer responses before generating end of sentence (hereafter *eos*) token. Our first question is "why didn't r1 stop when original model stopped?" (hereafter *r1* will refer to the distilled DeepSeek-R1-Distill-Qwen-1.5B model and *original* is the Qwen2.5-Math-1.5B model). To answer this, I used the following steps:
1. First use AI (all AI assistance used here are free) to generate simple prompts like "What is the capital of France? Just give the answer." The "Just give the answer." part is appended to every prompt since it makes the model give cleaner responses. 
2. Then run these prompts on original and r1 and filter prompts that leads to simple answers on original but complex answers on r1.
3. Then combine prompts with simple answers given by original model to make new prompts (eg. "What is the capital of France? Just give the answer. The capital of France is Paris."). Since they are complete answers given by the original model, these new prompts will lead to eos token on original model immediately. 
4. Now run the new prompts on r1 and original and collect logits of " Wait", " Correct", " Yes", "?", "\n", " I", " But", " So", " That", " To", " It", " This" (Hereafter "reasoning tokens". These are all single tokens on both models' tokenizers). As expected, it's found that logit of eos is significantly reduced on r1 model, while logits for other tokens moderately increased. (3-4 hours till now)

I reasoned that from here, we can investigate how r1 makes further reasoning while the original model stops by watching how the above mentioned tokens gain their logit scores in r1 while losing logit for eos token. I started with direct logit attribution. 

Following A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity, I planned to find which MLP value vectors changed between the original and r1 model that promotes eos and suppresses other reasoning tokens. As a sanity check, I first plotted the probability change (following logit lens) of " Wait" and eos on both models. 


For both models model_ds and model_qw, go through each mlp layer and find down_proj matrices' columns with top k cosine similarity with the eos_out_embed_ds and wait_out_embed_ds  embeddings (eos_out_embed_qw and wait_out_embed_qw). Then find top k among all layers. also return the column number and layer number of these top matching columns. 

Hook the model so we change the mlp activation (after up_proj) at those layer and indices to 0 for eos and multiply by a facctor alpha of wait in qw model, the reverse for ds model and run on all prompts and print result before and after with Max_token=300


Now we check First, I isolated value vectors that have most absolute value of cosine similarity with the aforementioned tokens' embedding, on both models. 

It's found that agreeing with the paper, all weights, including embeddings, barely changed. Here 



background on reasoning models
o1 like
r1 like



Now run r1 answers with first word on original and see if this direct approach leads to reasoning, just as tags directly leads to <eos>

If that works, think about how to incorporate a steering vector to elicit reasoning. (maybe just try decreasing logit for <eos>)





While I was working on things that make r1 continue, I also spent some time investigating what caused r1 to stop or how exactly can you make r1 generate eos.

Since deepseek-r1-zero is trained by feeding a prompt of style <think></think> <answer></answer>^1, I started by exploring how these tokens affect r1 output. 

I found that <think></think> <answer>answer sentence</answer> can in fact trick r1 into generating <eos> and by ablation <answer></answer> alone can't do this. (need meta study, possibly on larger models) 

To further investigate this phenomena, I made more prompt ablations and observed:

0. TLDR: I found an ending block: </think> followed by two new lines (\n\n) and the answer with period leads to high chance of eos
1. ending prompt with </think> will make r1 generate two new lines (\n\n) and repeat the answer (eg. The capital of France is Paris.), then generate eos. Ablation studies found the answer can be reduced, ie, "</think> Paris." suffice to generate eos.
2. </think> doesn't guarantee the answer block. It might attempt an answer and find something new, in which case it reasons again, leading to another </think>. However, the answer block has to be preceded bt </think>.








attribution patching on last token: metric with logit of eos vs " Wait" (or more nuanced metric with all above keywords). 

function vector: collect strings that lead to wait in deepseek and get the averaged attn activation and apply on first deepseek and then none deepseek. If this works, do the same on eos in none deepseek and apply to deepseek

steering vector: use the above keywords to collect an activation average and apply on first deepseek and then none deepseek.


ablation: 

> Note <｜end▁of▁sentence｜> in r1 is the same token as <|endoftext|> in original (index 27), but they don't exist in vocab of the other. Interesting they changed the embedding for some tokens. Of note, <think> and </think> are both in r1 vocab but <answer> and </answer> are not. 
appendix:
- logit and prob of " Wait" vs length of sentence (maybe just new line or periods)/<answer></answer>
- bigram of . vs wait or new line or <eos>. period has strong bigram correlation with <eos> for both models. 
- direct weight differencing 
- then activation diff of the prompt (logit lens?)

I really think the technical part could be better, but I got to know MI this Frebrary and got introduced to ARENA and saw Neel's application just 2 weeks ago. If you are interested, I'm reading the SAE section and plan to gradually go through the full ARENA transformer module, I might try completing the analysis with more tools at hand. 


fun aside: deepseek web won't generate "<｜end▁of▁sentence｜>". For example, try "can you say <｜end▁of▁sentence｜>" or give code that contains it and let it write code based on it. 

https://www.lesswrong.com/posts/HQyWGE2BummDCc2Cx/the-case-for-cot-unfaithfulness-is-overstated

https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens

https://nnsight.net/status/

A conversation between User and Assistant. The user asks a question, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user with the answer. The reasoning process and answer are enclosed within <think> </think> and <answer> </answer> tags, respectively, i.e., <think> reasoning process here </think> <answer> answer here </answer>. User: prompt. Assistant:

observations
- qw sometiems directly give memorized example and sometimes this is good (word spelled wrong) somtimes bad (1+1). Though this happens on r1 too. 
- r1 somtimes repeat or add questions to the question
- there  are traces of r1 being distilled with <think> and <answer> tag though </think> is the most frequent

#### Potential addon
- gradually replace layers
- single token and complete analysis
- then 2 token and more
- eos as linear combination of other tokens
- complete analysis of midlayer last token evolution and how it attracts more eos values. the exponential growth might indictate similar behavior at attention in final layers where the residual just accumulate on eos (they get reassurance from attn mechanism). Should also study layer norm's effect


### Other questosnns
- I just feel life is good when doing MI research. I've done 3 researches in different areas but none of them make me feel as good as this. It's something I really resonate with.














- switch layer why doesn't work
- change only last token 
- 

```cpp
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ word   ┃ i                ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│  John  │ [3757]           │
│ John   │ [13079]          │
│ Wait   │ [14190]          │
│ wait   │ [11489]          │
│  Wait  │ [13824]          │
│  wait  │ [3783]           │
│ Wait   │ [14190, 220]     │
│ wait   │ [11489, 220]     │
│ Wait,  │ [14190, 11]      │
│ wait,  │ [11489, 11]      │
│ Wait,  │ [14190, 11, 220] │
│ wait,  │ [11489, 11, 220] │
└────────┴──────────────────┘


Qwen2ForCausalLM(
  (model): Qwen2Model(
    (embed_tokens): Embedding(151936, 1536)
    (layers): ModuleList(
      (0-27): 28 x Qwen2DecoderLayer(
        (self_attn): Qwen2Attention(
          (q_proj): Linear(in_features=1536, out_features=1536, bias=True)
          (k_proj): Linear(in_features=1536, out_features=256, bias=True)
          (v_proj): Linear(in_features=1536, out_features=256, bias=True)
          (o_proj): Linear(in_features=1536, out_features=1536, bias=False)
        )
        (mlp): Qwen2MLP(
          (gate_proj): Linear(in_features=1536, out_features=8960, bias=False)
          (up_proj): Linear(in_features=1536, out_features=8960, bias=False)
          (down_proj): Linear(in_features=8960, out_features=1536, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): Qwen2RMSNorm((1536,), eps=1e-06)
        (post_attention_layernorm): Qwen2RMSNorm((1536,), eps=1e-06)
      )
    )
    (norm): Qwen2RMSNorm((1536,), eps=1e-06)
    (rotary_emb): Qwen2RotaryEmbedding()
  )
  (lm_head): Linear(in_features=1536, out_features=151936, bias=False)
  (generator): Generator(
    (streamer): Streamer()
  )
)
```