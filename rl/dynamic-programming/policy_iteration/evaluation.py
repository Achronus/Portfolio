import gym
import numpy as np

class PolicyEvaluation:
  """
  A basic representation of Iterative Policy Evaluation.
  
  Parameters:
    env (gym.Env) - Gym environment
    gamma (float) - discount factor
    theta (float) - a very small value to handle the stopping criteria
  """
  def __init__(self, env: gym.Env, gamma: float, theta: float) -> None:
    self.env = env
    self.gamma = gamma
    self.theta = theta

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

  def _act(self, V: np.array, state: int, policy: np.array, Vs: float) -> float:
    """
    Helper function used to update the value of state and returns it.
    
    Parameters:
      V (np.array) - array containing the estimated values of state
      state (int) - current state value index
      policy (np.array) - agent policy
      Vs (float) - current value of state

    Returns:
      Vs (float) - updated value of state
    """
    # Iterate over each action
    for action, action_prob in enumerate(policy[state]):
      # Iterate over each set of one-step dynamics (env.P)
      for state_prob, next_state, reward, _ in self.env.P[state][action]:
        # Update value of state
        Vs += action_prob * state_prob * self._calc_discount(V, reward, next_state)
    return Vs

  def evaluate(self, policy: np.array) -> np.array:
    """
    Evaluates a given policy and returns its updated version.
    
    Parameters:
      policy (np.array) - agent policy

    Returns:
      V (np.array) - updated policy
    """
    V = np.zeros(self.env.nS) # contains all estimated values of state

    while True:
      delta = 0

      # Iterate over each state
      for state in range(self.env.nS):
        # Update all values of state
        Vs = self._act(V, state, policy, Vs=0)

        # Update delta to check how much Vs has changed
        delta = max(delta, np.abs(V[state] - Vs))
        V[state] = Vs # Update states value of state

      # Exit loop when delta is smaller than theta
      if delta < self.theta:
        break

    # Return updated policy
    return V
