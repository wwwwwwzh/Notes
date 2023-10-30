
# Convention
Note that A, S, O are space.
Also note that subscript t for any of the first section symbols mean the value of it at step t.

- S: state
- O: observation. partial state
- A: action
- τ: sequence of states and actions
- r: feedback I get from the environment after performing an action at a state. i.e.g. a golden apple gives reward of 5. So if I get a golden apple at t=3 without anything else happening, r3=5
- R: reward function from τ to real number. R(τ)=rt+γ[rt+1]+γ^2[rt+2]...

- π: Policy function from state to a probability distribution over the set of actions. i.e πθ(s)=P(A|s;θ). In huggingface's blog, π(at|st) is the probability of action at given st
- J: Objective function from space of  parametrization θ of policy to expected cumulative reward. J(θ) = ΣP(τ;θ)R(τ) written as Eτ~π(R(τ)). P(τ;θ) = $ΠP(s_{t+1}|s_t,a_t)\pi_\theta(a_t|s_t)$
- V: Value function from state to expected cumulative reward if following a certain policy. Note that R is deterministic while V is an expectation



RL is based on the reward hypothesis, which is that all goals can be described as the maximization of the expected return (expected cumulative reward).

# Policy Based
The main goal of Reinforcement learning is to find the optimal policy π* that will maximize the expected cumulative reward. Because Reinforcement Learning is based on the reward hypothesis: all goals can be described as the maximization of the expected cumulative reward.

## Policy Gradient
J(θ) = Eτ~π(R(τ)) = ΣP(τ;θ)R(τ). P(τ;θ) = $ΠP(s_{t+1}|s_t,a_t)\pi_\theta(a_t|s_t)$

### Problem of Optimization
- Calculating gradient of J involves calculating every probability of τ which is expensive (space of all states and all actions is huge).
- It also involves probability of the environment going into the next state, given the current state and the action taken by the agent, which we don't have

Solution: Policy Gradient Theorem

### Policy Gradient Theorem
https://huggingface.co/learn/deep-rl-course/unit4/pg-theorem

### Reinforce algorithm (Monte Carlo Reinforce)
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