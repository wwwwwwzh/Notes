
## Basics
### Env (gym.Env)
inherited
- np_random
    - func normal

common implemented
- var action_space
- var observation_space
- step(self, arm: ActType) -> tuple[obs:ObsType, reward:float, terminated:bool, truncated:dict]
- reset(seed)
- render() 

examples:
```py
gym.envs.registration.register(
    id="ArmedBanditTestbed-v0",
    entry_point=MultiArmedBandit,
    max_episode_steps=max_episode_steps,
    nondeterministic=True,
    reward_threshold=1.0,
    kwargs={"num_arms": 10, "stationary": True},
) # kwargs are the init args for MultiArmedBandit class

env = gym.make("ArmedBanditTestbed-v0")
print(f"Our env inside its wrappers looks like: {env}")
```


### Agent
- var rng: np.random.Generator
- get_action(self) -> ActType
- observe(self, action: ActType, reward: float, info: dict) -> None: 
- reset(self, seed: int) -> None

episode and run are the same. Usually we let an agent run many episodes

```py
while not done:
    arm = agent.get_action()
    obs, reward, terminated, truncated, info = env.step(arm)
    done = terminated or truncated
    agent.observe(arm, reward, info)
    rewards.append(reward)
```

### Bandit eg
![](/images/arena-rl-bandit-0.png)
this is ploted with utils.plot_rewards(all_rewards, names) where all_rewards is (3,200,1000). The 1000 means every episode/run has 1000 steps. The 200 means we run one episode on 200 agents. The plot x axis is step and y is reward averaged for 200 agents at that step.

## Value Iteration
$$
V_\pi(s) = \sum_a \pi(a \mid s) Q_\pi(s, a) \\

Q_\pi(s,a) = \sum_{s',r} p(s',r \mid s,a) \left( r + \gamma V_\pi(s')\right)
$$

We say that two policies $\pi_1$ and $\pi_2$ are **equivalent** if $\forall s \in S. V_{\pi_1}(s) = V_{\pi_2}(s)$. A policy $\pi_1$ is **better** than $\pi_2$ (denoted $\pi_1 \geq \pi_2$) if
$\forall s \in S. V_{\pi_1}(s) \geq V_{\pi_2}(s)$.

## TD Learning
- bellman
- monte carlo

## DQL

## Policy Gradient
We want to maximize policy wrt the culmulative expected reward $J(\theta)=E_{\tau\sim\pi_\theta}[G(\tau)]=E_{\tau\sim\pi_\theta}[\sum_t^T \gamma^t r(s_t, a_t)]$

Expanding the expectation: $J(\theta)=\int p(\tau|\theta)G(\tau)d\tau$

$\nabla J(\theta)=\int \nabla p(\tau|\theta)G(\tau)d\tau$. Since the gradient is on p, which is a product, we use the trick $\nabla x=x\nabla logx$ to convert it to $\int p(\tau|\theta) \nabla \log p(\tau|\theta)G(\tau)d\tau$. Notice that the gradient term can now be reduced to sum of gradients:

$\nabla J(\theta)=\int p(\tau|\theta) \nabla \log p(\tau|\theta)G(\tau)d\tau$

$p(\tau|\theta)=\mu(s_0) \prod_t \pi(a_t|s_t)P(s_{t+1}|s_t,a_t)\\ \log p(\tau|\theta)=\log \mu(s_0) + \sum_t \log \pi(a_t|s_t)+\log P(s_{t+1}|s_t,a_t)\\ \nabla \log p(\tau|\theta)=\sum_t \nabla \log \pi(a_t|s_t)$

$\nabla J(\theta) = \int p(\tau|\theta) \sum_t \nabla \log \pi(a_t|s_t)G(\tau)d\tau \\= E_{\tau\sim\pi_\theta}[\sum_t \nabla \log \pi(a_t|s_t)G(\tau)]$

### Actor Critic

### PPO


## RLHF
- pretrained LLM
- By comparing model outputs in head-to-head matchups, an Elo system can be used to generate a ranking of the models and outputs relative to each-other. These different methods of ranking are normalized into a scalar reward signal for training.
- At this point in the RLHF system, we have an initial language model that can be used to generate text and a **preference model** that takes in any text and assigns it a score
- fine-tune some or all of the parameters of a copy of the initial LM with a policy-gradient RL algorithm, Proximal Policy Optimization (PPO). Some parameters of the LM are frozen because fine-tuning an entire 10B or 100B+ parameter model is prohibitively expensive (for more, see Low-Rank Adaptation (LoRA) for LMs or the Sparrow LM from DeepMind)
- Let's first formulate this fine-tuning task as a RL problem. First, **the policy is a language model** that takes in a prompt and returns a sequence of text (or just probability distributions over text). The action space of this policy is all the tokens corresponding to the vocabulary of the language model (often on the order of 50k tokens) and the observation space is the distribution of possible input token sequences, which is also quite large given previous uses of RL (the dimension is approximately the size of vocabulary ^ length of the input token sequence). The reward function is a combination of the preference model and a constraint on policy shift.
