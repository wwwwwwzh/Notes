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