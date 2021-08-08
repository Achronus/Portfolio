import gym
import numpy as np

from improvement import PolicyImprovement

class ValueIteration:
  """
  A basic representation of Value Iteration.
  
  Parameters:
    env (gym.Env) - Gym environment
    gamma (float) - discount factor
    theta (float) - a very small value to handle the evaluations stopping criteria
  """
  def __init__(self, env: gym.Env,gamma: float = 1.0, theta: float = 1e-8) -> None:
    self.env = env
    self.gamma = gamma
    self.theta = theta

    self.pol_imp = PolicyImprovement(env, gamma)
  
  def evaluate(self, V: np.array, delta: float) -> tuple:
    """
    Performs a single step of Policy Evaluation and returns the updated values of state and the change in policies (delta).
    
    Parameters:
      V (np.array) - agent policy
      delta (float) - change in policy

    Returns: 
      V, delta (tuple) - updated agent policy and updated change in policy
    """
    # Iterate through each state
    for state in range(self.env.nS):
      # Set value of state
      v = V[state]

      # Update the new value of state
      V[state] = max(self.pol_imp.convert_v_to_q(V, state))

      # Calculate delta change
      delta = max(delta, abs(V[state] - v))
    
    return V, delta

  def iterate(self, policy: np.array) -> tuple:
    """
    Performs Value Iteration by calculating the action-values and iteratively improving a given policy. Returns an environments optimal policy and value function.
    
    Parameters:
      policy (np.array) - agent policy

    Returns:
      policy, V (tuple) - the optimal policy and optimal action-value function
    """
    V = np.zeros(self.env.nS) # contains all estimated values of state

    while True:
      delta = 0

      # Evaluate the policy once
      V, delta = self.evaluate(V, delta)
      
      # Stop iterating if delta is optimal
      if delta < self.theta:
        break
    
    # Update the policy
    policy = self.pol_imp.improve(V, policy)

    # Return optimal policy and action-value function
    return policy, V
