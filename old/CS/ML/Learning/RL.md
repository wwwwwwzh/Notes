# Introduction
RL is based on the reward hypothesis: all goals can be described as the maximization of the expected cumulative reward. It's used when data are not or sparsely "labeled". (This means, for example, if your goal is to "succeed", then you can quantize this goal by believing, say, that success means maximization of money and fame. In addition, this means each intermediate position has a definite value such that to maximize the final goal you need to maximize each intermediate goal. For example, you might need to be in a good school at 18, have a good family at 30 etc.)

But unlike supervised learning (SL) which has a known label for every training point, RL doesn't have reward for each step, thus it learn by trial and error. The Markov assumption seems to imply that we can find the exact good actions of a given state no matter what the history or future of states are (a MLP from state to action). But we can't collect all the (state,action) pairs because we don't know if a specific action at a state is good or not. Further, the state space is just too big and by interaction we encounter those likely ones. (see offline training)


# Convention
Note that A, S, O are space.
Also note that subscript t for any of the first section symbols mean the value of it at step t.

- S: state
- O: observation. partial state
- A: action
- τ: sequence of states and actions
- r: S,A→R. feedback I get from the environment after performing an action at a state. i.e.g. a golden apple gives reward of 5. So if I get a golden apple at t=3 without anything else happening, r3=5
- R: τ→R. reward function from τ to real number. R(τ)=rt+γ[rt+1]+γ^2[rt+2]...

- V: S→R. Value function from state to expected cumulative reward if following a certain policy. Note that R is deterministic while V is an expectation
- π: S→P(A). Policy function from state to a probability distribution over the set of actions. i.e πθ(s)=P(A|s;θ). In huggingface's blog, π(at|st) is the probability of action at given st
- J: Θ→R. Objective function from space of  parametrization θ of policy to expected cumulative reward. J(θ) = ΣP(τ;θ)R(τ) written as Eτ~π(R(τ)). P(τ;θ) = $ΠP(s_{t+1}|s_t,a_t)\pi_\theta(a_t|s_t)$




RL is based on the reward hypothesis, which is that all goals can be described as the maximization of the expected return (expected cumulative reward).

# Policy Based
The main goal of Reinforcement learning is to find the optimal policy π* that will maximize the expected cumulative reward. Because Reinforcement Learning is based on the reward hypothesis: all goals can be described as the maximization of the expected cumulative reward.

## Policy Gradient
Subclass of Policy based methods that uses gradient method (gradient ascent on J)

J(θ) = Eτ~π(R(τ)) = ΣP(τ;θ)R(τ). P(τ;θ) = $ΠP(s_{t+1}|s_t,a_t)\pi_\theta(a_t|s_t)$

### Comparison
- Good on high dimensional space because it outputs a parametrizable distrbution.
- Smoother training

- Easy to converge on local minima
- Slower
- High variance

### Problem of Optimization
- Calculating gradient of J involves calculating every probability of τ which is expensive (space of all states and all actions is huge).
- It also involves probability of the environment going into the next state, given the current state and the action taken by the agent, which we don't have

Solution: Policy Gradient Theorem

### Policy Gradient Theorem
https://huggingface.co/learn/deep-rl-course/unit4/pg-theorem

### Reinforce algorithm (Monte Carlo Reinforce)
![](/images/policy_gradient.png)
![](/images/policy_gradient_multiple.png)


# Value Based
you don’t train the policy: your policy is just a simple pre-specified function (for instance, the Greedy Policy) that uses the values given by the value-function to select its actions.
In fact, most of the time, in value-based methods, you’ll use an Epsilon-Greedy Policy.

Value based approach is indirect compared to policy based method. The value function makes it possible for a greedy policy to achieve max reward. However, viewed in another way, they are essentially the same because value of an action can be viewed as the unnormalized probability of taking that action. 

### State Value Function
From state to value. It should mean that if we follow a certain predefined policy, how much we want our state to be at a particular state.

### Action Value Function
From state and action to value

## Learning Algorithm
### Monte Carlo
Uses an entire episode of experience before learning. 

- Let agent go with current V
- After one episode, get Gt which is the return
- Gt-V(St) is the update direction

### Temporal Difference
Uses one step (st,at,st+1,at+1) to learn

## Q-Learning
Q-Learning is an off-policy value-based method that uses a TD approach to train its action-value function called Q-function.

This is a pretty traditional algorithmic approach to learning where our behavior of learning by reinforcement/reward is hand coded to an algorithm.

### Q-Table
Table with value for all state-action pairs

### ε-greedy Policy
Choose best action with p=1-ε, randomly with p=ε. We progressively reduce the epsilon value since we will need less and less exploration and more exploitation. Note that this is used in training only.

### Q-Learning Algorithm
1. Initialize the table with all 0
2. Use ε-greedy policy to select an action
3. Take the action and compute reward
4. Update Q-table with the observed reward
5. Repeat from 2

```py
action=epsilon_greedy_polic(Qtable, state, epsilon)

new_state, reward,terminated, truncated, info= env.step(action)

Qtable[state][action] =Qtable[state][action] +learning_rate * (
    reward + gamma * np.max(Qtable[new_state]) - Qtable[state][action]
)
# If terminated or truncatedfinish the episode
if terminated or truncated:
    break

state = new_state
```

### Deep Q-Learning
The Q-table size is #(S)*#(A). In a very very simple 4x4 tile based game, this is just 16x4=64. However,  the state space in Atari games can contain 10^9 to 10^11 states.

Solution is to replace the table with a deep Q-network (DQN)

# A2C
Monte-Carlo sampling to estimate return has significant variance in policy gradient estimation.

Solution:
- An Actor that controls how our agent behaves (Policy-Based method) πθ(s)
- A Critic that measures how good the taken action is (Value-Based method) q(a,s)

# Offline Learning
Online learning is based on the intuition that we humans learn by trial and error and we can gradually Monte Carlo to the best policy. 

The key advantage is that we can sample from the enormous state space and use simple rewards.

If we try to train robots e.g. driver in supervised fashion, what will be the challenges?

## Why Not Supervised 
1. The state space is too big and plausible state space is also big. So there will likely be distribution shift.
2. We don't know the "correct" action given state. We simply can't collect all best state action pairs. (In imitation learning, we simply say all demonstrations are good)
3. If we just use a final reward we risk ignoring the good part of a bad episode or emphasizing the bad part of a good episode. (Like in imitation learning, some sub-optimal actions are learned) 
4. Even if our generalization is good, there will be points where network prediction is very off and lead the agent to underrepresented state trajectory. 

### Distribution Shift
![](/images/distribution-shift.png)
![](/images/distribution-shift-1.png)

# Others
### [RLHF](https://huggingface.co/blog/rlhf)
RLHF has enabled language models to begin to align a model trained on a general corpus of text data to that of complex human values.

Process: initial LLM->optional supervised fine-tuning with "expensive augmented data" (text with specific criteria like human value)->train reward model (from scratch or from a LM)->copy and finetune the LLM with RL (KL from original to avoid fooling the RM, r=r-KL)
![](/images/rlhf.png)
![](/images/rlhf-2.png)