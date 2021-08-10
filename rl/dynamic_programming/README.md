# Dynamic Programming

## Description

This repository focuses on Dynamic Programming (DP) methods that use a single OpenAI Gym environment: `FrozenLake-v0`. The DP setting requires agents to have full knowledge of the Markov Decision Process (MDP) that they are trying to solve. While this is easier than the traditional Reinforcement Learning (RL) setting, it is fundamental in understanding the basic principle of RL algorithms.

## Project Implementations

There are three types of implementations to solve the `FrozenLake` environment: Policy Iteration, Truncated Policy Iteration, and Value Iteration.

Policy Iteration uses a sequence of policy evaluation and improvement steps that guarantees convergence to an optimal policy when applied to a finite MDP. Comparatively, Truncated Policy Iteration is a modified version of Policy Iteration that limits the evaluation step to a maximum number of iterations through the space state. The final type of Policy Iteration is Value Iteration. It performs a single evaluation step before improving the given policy until it converges to the optimal one.

- [Policy Iteration](https://github.com/Achronus/Portfolio/tree/master/rl/dynamic_programming/policy_iteration)
- [Truncated Policy Iteration](https://github.com/Achronus/Portfolio/tree/master/rl/dynamic_programming/truncated_policy_iteration)
- [Value Iteration](https://github.com/Achronus/Portfolio/tree/master/rl/dynamic_programming/value_iteration)

Each implementation achieves an optimal policy and optimal state-value function, outlined below:

```Python
# Optimal Policy (LEFT = 0, DOWN = 1, RIGHT = 2, UP = 3):
[[1.   0.   0.   0.  ] 
 [0.   0.   0.   1.  ]  
 [0.   0.   0.   1.  ]  
 [0.   0.   0.   1.  ]  
 [1.   0.   0.   0.  ]  
 [0.25 0.25 0.25 0.25]  
 [0.5  0.   0.5  0.  ]  
 [0.25 0.25 0.25 0.25]  
 [0.   0.   0.   1.  ]  
 [0.   1.   0.   0.  ]  
 [1.   0.   0.   0.  ]  
 [0.25 0.25 0.25 0.25]  
 [0.25 0.25 0.25 0.25]  
 [0.   0.   1.   0.  ]  
 [0.   1.   0.   0.  ]  
 [0.25 0.25 0.25 0.25]] 
```

```Python
# Optimal State-Value Function:
[0.82352 0.82352 0.82352 0.82352 
 0.82352 0.      0.52941 0.         
 0.82352 0.82352 0.76470 0.
 0.      0.88235 0.94117 0.     ]
```
