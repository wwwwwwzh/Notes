

# Introduction
> The major diference btw RL and supervised learning (SL) is the separation of action and reward. In SL, we have the correct action. In RL, we need to learn actions from **reward that does not rely on knowledge of the correct action**. This means RL need to solve the credit assignment problem. In addition, Harry Klopf argued that SL lacked "hedonic aspects of behavior". Thus RL can be seen as active while SL passive. See [more comparison btw the learning methods](/intelligence.md#machine-learning)
## History
- Three threads came together in the 90s that made modern RL
    - cognitive science
        - Edward Thorndike and Law of Effect
        - Pavlov described reinforcement as the strengthening of a pattern of behavior due to an animal receiving a stimulus—a reinforcer—in an appropriate temporal relationship with another stimulus or with a response.
        - many people (Turing, Shannon, Minsky, etc) have since built electro-mechanical machines to demonstrate law of effect. 
        - However, many people soon started doing supervised learning but kept using reinforcement language, creating confusion
    - optimal control: 
        - late 1950s
        - described the problem of designing a controller to minimize or maximize a measure of a dynamical system’s behavior over time. 
        - Bellman and others extended Hamilton and Jacob's dynamical state functional to Bellman equation (or HJB equation)
        - the methods for solving the HJB are known as dynamic programming; the discrete stochastic version of HJB is called Markov Decision Process (MDP)
        - curse of dimensionality
    - temporal difference learning
        - secondary reinforcer
        - Claude Shannon’s (1950) suggestion that a computer could be programmed to use an evaluation function to play chess, and that it might be able to improve its play by modifying this function online.
        - Sutton (1978a,b,c) described learning rules driven by changes in temporally successive predictions. 

![](/images/rl-ttt.png)



# Tabular Methods
## Multi-armed Bandit
symbols
- A: random variable denoting action, or set of actions
- R: random variable denoting reward, or set of rewards, or real numbers
- q*: A->R, action value, q*(a)=E[Rt|At=a]
- Qt(a): A->R, estimate for action value

k-armed bandit
- repetitively playing a k-armed bandit: at t, do At (A1 or A100 are instantiations of action rv, but At is still considered rv) and receive Rt. The conditional reward distribution P(Rt|At) doesn't change with time.
- the value of an action is the expected reward of the action: **q*(a)**=E[Rt|At=a]
- estimate of value of an action **Qt(a)** which is a set of functions A->R 
- a set of method for estimating value function is called action-value methods. The naive way is to take the average reward for a given action
- The naive way to select an action once Q has been estimated is to take At=argmaxQt(a). This is called **greedy** action selection method. The initial values are all 0.
- We can also select greedily most of time but with **ε** probability select (uniform) randomly among all actions.
- **10-armed bandit testbed**: 10 armed bandit where q* is normal around a standard normal mean and var=1. We test an algorithm by running it for 1000 steps on this problem and this is one run. We then generate another 10 armed bandit problem. Do this 2000 times so we have 2000 runs. ![](/images/10-armed-testbed-1.png)![](/images/10-armed-testbed.png) The graph has steps as x axis. eg. at step=100, it means we have 2000 identical algorithms running on 2000 10-armed bandit problems and t=100 for each one, and vertical axis is the average reward at t=100. ε=0.1 never fully converge to maximum of 1.54 because 10% of time it chooses non optimal solutions.
> note that neither graph have converged. For epsilon=0.1 the eventual optimal action will take 91% but is growing slowly at this point in the graph because action 3 and 5 are very similar in distribution. epislon=0.01 would eventually reach >99% optimal action.
- Incremental learning (infinite moving average): 
- recency-weighted average for non stationary problem
- otimistic initial value: replace the 0 initial values for greedy to higher number
- 

## MDP
![](/images/rl-recycle-bot.png)
Value function and action-value function
- This shows value of each state using a uniform random policy ![](/images/rl-grid-world.png)

Bellman equation for v
- ![](/images/bellman.png)
- Compare [HJB](/reference.md#hjb)

Bellman optimality equation for v* and q*
- ![](/images/bellman-op-v.png)
- ![](/images/bellman-op-q.png)
- ![](/images/rl-grid-world-op.png)

## Dynamic Programming (DP)
The term dynamic programming (DP) refers to a collection of algorithms that can be used to compute optimal policies given a perfect model of the environment as a Markov decision process (MDP). The key idea of DP, and of reinforcement learning generally, is the use of value functions to organize and structure the search for good policies.

### Policy Eval
iteratively evaluate the value of state so the correctness "ripples off"
![](/images/policy-eval.png)

### Policy Improvement

### Policy Iteration
![](/images/policy-iter.png)

### Value Iteration
![](/images/value-iter.png)

## Monte Carlo Methods
![](/images/FV-MC.png)
![](/images/MC-ES.png)
![](/images/MC-control-on.png)
![](/images/MC-control-off.png)

## Temporal Difference
TD learning is a combination of Monte Carlo ideas and dynamic programming (DP) ideas

# Non Book Material
## Model Free
### Policy Gradient
We want to maximize policy wrt the culmulative expected reward $J(\theta)=E_{\tau\sim\pi_\theta}[G(\tau)]=E_{\tau\sim\pi_\theta}[\sum_t^T \gamma^t r(s_t, a_t)]$

Expanding the expectation: $J(\theta)=\int p(\tau|\theta)G(\tau)d\tau$

$\nabla J(\theta)=\int \nabla p(\tau|\theta)G(\tau)d\tau$. Since the gradient is on p, which is a product, we use the trick $\nabla x=x\nabla logx$ to convert it to $\int p(\tau|\theta) \nabla \log p(\tau|\theta)G(\tau)d\tau$. Notice that the gradient term can now be reduced to sum of gradients:

$\nabla J(\theta)=\int p(\tau|\theta) \nabla \log p(\tau|\theta)G(\tau)d\tau$

$p(\tau|\theta)=\mu(s_0) \prod_t \pi(a_t|s_t)P(s_{t+1}|s_t,a_t)\\ \log p(\tau|\theta)=\log \mu(s_0) + \sum_t \log \pi(a_t|s_t)+\log P(s_{t+1}|s_t,a_t)\\ \nabla \log p(\tau|\theta)=\sum_t \nabla \log \pi(a_t|s_t)$

$\nabla J(\theta) = \int p(\tau|\theta) \sum_t \nabla \log \pi(a_t|s_t)G(\tau)d\tau \\= E_{\tau\sim\pi_\theta}[\sum_t \nabla \log \pi(a_t|s_t)G(\tau)]$

In practice, we run the policy from a state for some time T (could be fixed or variable) and stop and call it an episode. For each episode, we calculate G(t) for all t.

> !Important Note! All these math means that by applying the likelihood‐ratio (or “log‐derivative”) trick and using the fact that the environment’s transition probabilities $P(s_{t+1}\mid s_t,a_t)$ do not depend on 𝜃, we convert one big gradient over entire trajectories into a sum of per‐time‐step terms. 

### Actor Critic
Summary
- Instead  of running the whole episode, at each t, 
- immediately update the critic with the a MSE with the temporal difference error: $  δₜ = rₜ + γV_φ(s_{t+1})-V_φ(s_t)$, 
- also immediately update the actor with the "advantage", $\nabla_θ \log π_θ(aₜ|sₜ) \times δ_t$
- For steps without reward, we either use r=0 which is fine or invent some pseudo-rewards based on how “surprised” our agent is. Some common rewards are prediction error reward and novel or rarely visited states reward, both to boost exploration

> intuitively, we as humans keep an inner voice, whenever we make actions, as a critic. This is very efficient because we can't keep too much working memory and update our policy only after we receive the actual reward, which may take a very long time. Thus this intuitively makes training the computer more stable. 

Neuroscience
- This resembles actual brain. The actor is the cortico-striatal circuits in the basal ganglia, and the critic is the dopaminergic neurons.
- Unexpected reward delivery (you expected nothing, then got a reward) elicits a large, transient increase in DA neuron firing—an action potential “burst.” Better-than-expected rewards have burst magnitude proportional to the surprise. This burst triggers synaptic plasticity in downstream targets (e.g. striatal neurons), reinforcing the actions or cues that led to the surprise 
- Omission of an expected reward (you expected food but receive none) causes DA neurons to pause or dip below baseline firing at the precise moment the reward was due, weakening synaptic associations that predicted the missing reward.
- Dopaminergic synapses on striatal medium spiny neurons use these bursts/dips to gate plasticity via D1 vs D2 receptor pathways—positive errors favor D1‐mediated potentiation, negative errors favor D2‐mediated depression
- Once a cue (e.g., a tone signaling reward) reliably predicts the outcome, the DA burst shifts forward to the cue’s onset—no longer bursting at reward delivery because it’s fully predicted. If the reward is then unexpectedly omitted after the cue, a dip still occurs at the expected reward time, demonstrating the system’s precise temporal coding of prediction errors
- Rescorla–Wagner model of conditioning (Learning happens when there’s surprise)


### PPO


### RLHF
reward model
- Process supervised (PRM): sample：a=5-2，b=a+1，b?<step1_start> a=5-2=3<step1_end> <step2_start> b=3+1=4<step2_end>
- Outcome supervised (ORM)
- Distribution shift (with original model) penalty

Pipeline
- we have pretrained LLM
- Train reward model: By comparing model outputs in head-to-head matchups, an **Elo system** can be used to generate a ranking of the models and outputs relative to each-other. These different methods of ranking are normalized into a scalar reward signal for training.
- At this point in the RLHF system, we have an **initial language model** that can be used to generate text and a **preference model** that takes in any text and assigns it a score
- Train LLM with reward: fine-tune some or all of the parameters of a copy of the initial LM with a policy-gradient RL algorithm, Proximal Policy Optimization (**PPO**). Some parameters of the LM are frozen because fine-tuning an entire 10B or 100B+ parameter model is prohibitively expensive (for more, see Low-Rank Adaptation (LoRA) for LMs or the Sparrow LM from DeepMind)
- PPO: First, **the policy is a language model** (copy of the initial LLM) that takes in a prompt and returns a sequence of text (or just probability distributions over text). The action space of this policy is all the tokens corresponding to the vocabulary of the language model (often on the order of 50k tokens) and the observation space is the distribution of possible input token sequences, which is also quite large given previous uses of RL (the dimension is approximately the size of vocabulary ^ length of the input token sequence). The reward function is a combination of the preference model and a constraint on policy shift.
![](/images/rlhf-2.png)

> Note that this is model free since we are not simulating the environment dynamics (simulate sequences and corresponding rewards) but just training the policy model. However, the next token generation model can be seen as a model and there are ways to train model based RL on LLM.

### Direct preference optimization (DPO)
https://zhuanlan.zhihu.com/p/721073733

no RL, implicit reward model. 

### GRPO 
https://zhuanlan.zhihu.com/p/20812786520
https://www.zhihu.com/question/10766825126/answer/88583863333


## Model Based
### MCTS
According to predictive coding theory, one of the priamry fucntions of the cortex is to learn to model the world. This is done by constantly "predicting" the world. At every moment, we observe the world and predict the next state of the world. If it surprises you, you update the model. Thus we have a very good prediction model of the world.

However, the prediction model predicts next instance. Goal directed behaviors ususally require a long planning horizon. Thus we need to use our world model to simulate the long horizon before making the decision. Note that this is also a dimensionality problem. Each task requires choosing from number of state to the time length of the task, which is prohibitively large. It's not efficient to just learn every task as we learn every world state transition over short time window. 

Pipeline
1. At ffirst step, use current state as root node and build a tree
2. choose one action with upper conidence bound, get to next state, if it's not visited, roll out its subsequent actions using a model or randomly
3. update the value of the state and action and go back to root 
4. repeat 2 and 3
5. for each step, use the subtree and repeat 2,3,4

RLHF+MCTS
- the roll out is done by the LLM and the value is given by the reward model.