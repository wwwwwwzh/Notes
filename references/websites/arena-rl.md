
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

