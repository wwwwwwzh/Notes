# Notes
## Common Methods
### Imitation Learning
Imitation learning methods seek to construct a policy that accurately models the distribution of behavior in some dataset D = {(oi, ai)} , i ∈ {1...N} of action-observation pairs.

### Dynamics Model

### Inverse Dynamics Model
p(at|o1...oT)

# Dataset
## Manipulation
### [Meta World](https://meta-world.github.io/)

## Navigation
### [Habitat](https://aihabitat.org/)
- ObjectNav and ImageNav (go to/find [object])

## Others
- https://github.com/ScaledFoundations/GRID-playground

# Classical RL
## Others
### [Human-to-Robot Imitation in the Wild]()
- Summary: instruction video->prior(sequence of control actions)->VAE to represent policy centered on prior->minimize end result by comparing images after action

# (Semi-)Supervised
## Vision Based
- NF: Next Frame
- A: Output Action
- VQA: Visual Question Answering
- TMAE: Temporal Masked Autoencoder
- SMAE: Spatial Masked Autoencoder
- TSMAE: Temporal Spatial Masked Autoencoder

### [Dreamer 2019](https://arxiv.org/pdf/1912.01603.pdf)
- Summary: Dreamer uses a latent dynamics model that consists of three components. The
*representation model* next state given last state, last action and current observation. The
*transition model* predicts future model states without seeing the corresponding observations that will later cause them. The reward model predicts the rewards given the state.
- Arch: ![](/images/dreamer.png)

### NF Trajectory Transformer
- Summary: Model RL problem as sequence prediction with transformer
- Network: all previous (s1-sm, a1-an, reward) -> current+next frame. state and action discretized

### A [Vision Transformer Quadrupedal Locomotion 2021](https://arxiv.org/pdf/2107.03996.pdf)
- Summary: RL with a Transformer that learns to combine proprioceptive information and high-dimensional depth sensor inputs.
- Network: Proprioceptive state+past actions [31x3frames] (MLP) + depth images [64x64x4frames] (CNN) ->transformer->Proprioceptive feature+visual feature->action/reward
![](/images/vision-t-locomotion.png)
- Thought: they are still thinking in old RL context to output action and train with PPO. they should train next frame state and visual prediction and action so their network understands everything better

### [GATO 2022]()
- Summary: Generalized agent as supervised transformer with diverse tasks and dataset
- Network: ![](/images/gato.png)
- Dataset:

### A [RT-1 2022]()
- Summary: high-capacity architectures with open-ended task-agnostic training
- Dataset: 130k demonstrations of 700 tasks. ![](/images/rt-1-data.png)
- Network: 6 images + instruction -> ENet+TokenLearner -> Transformer -> Action (discretized)
![](/images/rt-1.png)

### A VQA [RT-2 2023]()
- Summary: pretrained visual language model (Visual Question Answering/VQA) to output action as text token directly
- Network: Image+Question/Task->Action ![](/images/rt-2.png)
- Thought: Humans connect actions with proprioception and vision first, then they use sound and later language to connect to these hidden ideas within those aforementioned connections. Human languages, taken for itself, because they are fundamentally connected to (or can be said to result from) real world things/senses, contain structures of the world. So language also already has structures for human actions that could be easily decoded to produce either robotic or human action command. So is it necessary to use visual prediction to further constrain and empower the structure of such network? 

### SMAE [VisualCortex-1 2023]()
- Summary: Large ViT model trained with MAE on 9 datasets as backbone and standard RL (Policy network) for 7 tasks. Comparable performance with SOTA PVR. Improvements upon adaptation (end to end finetuning or finetuning MAE with domain specific)
![](/images/vc-1.png)

### A SMAE [Real-World Robot Learning with Masked Visual Pre-training 2022](https://arxiv.org/pdf/2210.03109.pdf)
- Summary: Pretrained MAE, train separate control policy networks per task: input image features + proprioceptive states (joint positions) at t -> Action t + 1

### A SMAE [OVRL-V2 2023](https://arxiv.org/pdf/2303.07798.pdf)
- Summary: Simple pretrained ViT + LSTM + RL/Behavioral Cloning. 
- Network: ![](/images/OVRL.png)

### [Masked World Models for Visual Control 2022](https://proceedings.mlr.press/v205/seo23a/seo23a.pdf)
- Summary: inspired by dreamer + ViT MAE
- Arch: CNN token, ViT MAE+reward prediction, RNN dynamics

### [OpenAI VPT Minecraft 2022](https://openai.com/research/vpt)
- Summary: large unlabeled data pretraining for visual behavioral learning. Use Small labeled data to train inverse dynamics model (easier to train) + large unlabeled to get causal foundation model + additional RL finetuning 
- Arch: ![](/images/oa-vpt.png)
- Network: 128x128x128x3->temporal conv->ResNet->128x131072->MLP(256,4096)->128x4096->transformer->action