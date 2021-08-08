import copy
import gym
import numpy as np

from evaluation import PolicyEvaluation
from improvement import PolicyImprovement

class PolicyIteration:
  """
  A basic representation of Policy Iteration.
  
  Parameters:
    env (gym.Env) - Gym environment
    gamma (float) - discount factor
    theta (float) - a very small value to handle the evaluations stopping criteria
  """
  def __init__(self, env: gym.Env, gamma: float = 1.0, theta: float = 1e-8) -> None:
    self.env = env
    self.gamma = gamma
    self.theta = theta

    self.pol_eval = PolicyEvaluation(self.env, self.gamma, self.theta)
    self.pol_imp = PolicyImprovement(self.env, self.gamma)
  
  def iterate(self, policy: np.array) -> tuple:
    """
    Performs Policy Iteration, by evaluating a policy and then improving it. Returns an environments optimal policy and value function.
    
    Parameters:
      policy (np.array) - agent policy

    Returns:
      policy, V (tuple) - the optimal policy and optimal state-value function
    """
    while True:
      # Perform policy evaluation and get the state-value policy
      V = self.pol_eval.evaluate(policy) # np.array

      # Improve the policy by making it action-value
      new_policy = self.pol_imp.improve(V, policy) # np.array
      
      # Stop if value function estimate policies has converged
      new_V = self.pol_eval.evaluate(new_policy)
      if np.max(abs(V - new_V)) < self.theta * 1e2:
        break

      # Set best policy
      policy = copy.copy(new_policy)
    
    return policy, V
