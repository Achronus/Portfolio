import gym
import numpy as np

class TruncatedPolicyEvaluation:
  """
  A basic representation of Truncated Policy Evaluation. A type of Policy Evaluation that only performs a fixed number of sweeps through the state space.
  
  Parameters:
    env (gym.Env) - Gym environment
    max_sweeps (int) - number of sweeps until evaluation terminates
    gamma (float) - discount factor
  """
  def __init__(self, env: gym.Env, max_sweeps: int, gamma: float) -> None:
    self.env = env
    self.max_sweeps = max_sweeps
    self.gamma = gamma

  def _calc_discount(self, V: np.array, reward: float, next_state: int) -> float:
    """
    Helper function used to calculate and return the discount value.
    
    Parameters:
      V (np.array) - array containing the estimated values of state
      reward (float) - reward obtained from one-step dynamics
      next_state (int) - next state from one-step dynamics

    Returns:
      discounted_reward (float)
    """
    return reward + self.gamma * V[next_state]

  def convert_v_to_q(self, V: np.array, state: int) -> np.array:
    """
    Converts the state-values into action-values (q) and returns them.
    
    Parameters:
      V (np.array) - array containing the estimated values of state
      state (int) - current state value index

    Returns:
      action-values (np.array)
    """
    q = np.zeros(self.env.nA)
    # Iterate over each action
    for action in range (self.env.nA):
      # Iterate over each set of one-step dynamics
      for state_prob, next_state, reward, _ in self.env.P[state][action]:
        # Update the Q value for each action
        q[action] += state_prob * self._calc_discount(V, reward, next_state)
    # Return the updated values
    return q

  def update_value_of_state(self, policy: np.array, state: int, 
                            v: float, q: list) -> float:
    """
    Updates a value of state for a given policy and state. Returns the updated value.
    
    Parameters:
      policy (np.array) - agent policy
      state (int) - current state value index
      v (float) - current value of state
      q (list) - list of converted action-values

    Returns:
      v (float) - updated value of state
    """
    # Iterate through each action
    for action, action_prob in enumerate(policy[state]):
      v += action_prob * q[action]
    return v

  def evaluate(self, policy: np.array, V: np.array) -> np.array:
    """
    Evaluates a given policy and returns its updated version.
    
    Parameters:
      policy (np.array) - agent policy
      V (np.array) - an array containing the estimated values of state

    Returns:
      V (np.array) - updated policy
    """
    count = 0
    while count < self.max_sweeps:
      # Iterate over each state
      for state in range(self.env.nS):
        # Calculate all policy values
        v = 0
        q = self.convert_v_to_q(V, state)

        # Update value of state
        V[state] = self.update_value_of_state(policy, state, v, q)
      
      # Increment count
      count += 1

    # Return updated policy
    return V
