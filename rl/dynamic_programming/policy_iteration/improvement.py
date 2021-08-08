import gym
import numpy as np

class PolicyImprovement:
  """
  A basic representation of Iterative Policy Improvement.
  
  Parameters:
    env (gym.Env) - Gym environment
    gamma (float) - discount factor
  """
  def __init__(self, env: gym.Env, gamma: float) -> None:
    self.env = env
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

  def improve(self, V: np.array, policy: np.array) -> np.array:
    """
    Improves a given policy and returns its updated version.
    
    Parameters:
      V (np.array) - an array containing the estimated values of state
      policy (np.array) - agent policy

    Returns:
      policy (np.array) - updated policy
    """
    # Iterate over each state
    for state in range(self.env.nS):
      # Get the action-value policy
      q = self.convert_v_to_q(V, state)

      # OPTION 1: Construct a deterministic policy
      # policy[state][np.argmax(q)] = 1

      # OPTION 2: Construct a stochastic policy
      # Find best actions
      best_actions = np.argwhere(q == np.max(q)).flatten() # e.g. [0, 1, 2, 3] or [1, 2, 3]

      # Update state of policy (examples consist of four best actions):
      # 1. One hot encode each best action and store in a list of lists (np.eye) - e.g. 
      #    [np.array([1., 0., 0., 0.]), np.array([0., 1., 0., 0.]), np.array([0., 0., 1., 0.]), np.array([0., 0., 0., 1.])]
      # 2. Sum each best actions one hot encode and store in a list - e.g. 
      #    [1., 1., 1., 1.]
      # 3. Set equal probability for each action - e.g. 
      #    [1., 1., 1., 1.] / len(best_actions) = [0.25, 0.25, 0.25, 0.25]
      policy[state] = np.sum([np.eye(self.env.nA)[i] for i in best_actions], axis=0) / len(best_actions)
    
    # Return updated policy
    return policy
