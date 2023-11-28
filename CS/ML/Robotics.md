# Classical RL

# (Semi-)Supervised
## Transformer Based
### Trajectory Transformer
- Summary: Model RL problem as sequence prediction with transformer
- Network: all previous (s1-sm, a1-an, reward) -> current+next frame. state and action discretized

### [Vision Transformer Quadrupedal Locomotion 2021](https://arxiv.org/pdf/2107.03996.pdf)
- Summary: RL with a Transformer that learns to combine proprioceptive information and high-dimensional depth sensor inputs.
- Network: Proprioceptive state+past actions [31x3frames] (MLP) + depth images [64x64x4frames] (CNN) ->transformer->Proprioceptive feature+visual feature->action/reward
![](/images/vision-t-locomotion.png)
- Thought: they are still thinking in old RL context to output action and train with PPO. they should train next frame state and visual prediction and action so their network understands everything better

### RT-1 2022
- Summary: high-capacity architectures with open-ended task-agnostic training
- Dataset: 130k demonstrations of 700 tasks. ![](/images/rt-1-data.png)
- Network: 6 images + instruction -> ENet+TokenLearner -> Transformer -> Action (discretized)
![](/images/rt-1.png)
### RT-2 2023
- Summary: pretrained visual language model (Visual Question Answering/VQA) to output action as text token directly
- Network: Image+Question/Task->Action ![](/images/rt-2.png)
- Thought: Humans connect actions with proprioception and vision first, then they use sound and later language to connect to these hidden ideas within those aforementioned connections. Human languages, taken for itself, because they are fundamentally connected to (or can be said to result from) real world things/senses, contain structures of the world. So language also already has structures for human actions that could be easily decoded to produce either robotic or human action command. So is it necessary to use visual prediction to further constrain and empower the structure of such network? 

