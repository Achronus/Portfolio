import copy
import gym
import numpy as np

from evaluation import TruncatedPolicyEvaluation
from improvement import PolicyImprovement

class TruncatedPolicyIteration:
  """
  A basic representation of Truncated Policy Iteration.
  
  Parameters:
    env (gym.Env) - Gym environment
    max_sweeps (int) - number of sweeps until evaluation terminates
    gamma (float) - discount factor
    theta (float) - a very small value to handle the evaluations stopping criteria
  """
  def __init__(self, env: gym.Env, max_sweeps: int, gamma: float = 1.0, 
               theta: float = 1e-8) -> None:
    self.env = env
    self.max_sweeps = max_sweeps
    self.gamma = gamma
    self.theta = theta

    self.pol_eval = TruncatedPolicyEvaluation(env, max_sweeps, gamma)
    self.pol_imp = PolicyImprovement(env, gamma)
  
  def iterate(self, policy: np.array) -> tuple:
    """
    Performs Truncated Policy Iteration, by evaluating a policy and then improving it. Returns an environments optimal policy and value function.
    
    Parameters:
      policy (np.array) - agent policy

    Returns:
      policy, V (tuple) - the optimal policy and optimal state-value function
    """
    V = np.zeros(self.env.nS) # contains all estimated values of state

    while True:
      # Improve the policy
      policy = self.pol_imp.improve(V, policy)

      # Store old values of state
      old_V = copy.copy(V)

      # Update all values of state
      V = self.pol_eval.evaluate(policy, V)
      
      # Stop updating if theta has been achieved
      if np.max(abs(V - old_V)) < self.theta:
        break
    
    # Return optimal policy and value-function
    return policy, V
