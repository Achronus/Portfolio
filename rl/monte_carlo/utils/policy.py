from abc import ABC, abstractmethod

import gym
import numpy as np

class Policy(ABC):
  """A template class for policies."""
  @abstractmethod
  def __init__(self) -> None:
    pass

  @abstractmethod
  def set_policy(self) -> None:
    pass

class LimitedPolicy(Policy):
  """A basic representation of a limited policy that uses set probabilities for a given state. Used within the GenerateLimitedEpisodes class."""
  def __init__(self, stick_probas: list = [0.8, 0.2], threshold: int = 18) -> None:
    self.stick_probas = stick_probas
    self.hit_probas = stick_probas[::-1] # reversed
    self.threshold = threshold

  def set_policy(self, state: int) -> list:
    """Sets the policy for the given state based on the specified threshold, stick and hit probabilities. Returns a list of probabilities as a list."""
    return self.stick_probas if state[0] > self.threshold else self.hit_probas

  def Q_to_plot(self, Q: np.ndarray) -> dict:
    """Converts a given value function into a dictionary, in preparation for plotting."""
    v_dict = {}

    # Iterate over the value function
    for key, value in Q.items():
      # Calculate new value
      new_val = (key[0] > self.threshold) * self.__calc_dot(self.stick_probas, value) + \
      (key[0] <= self.threshold) * self.__calc_dot(self.hit_probas, value)
      # Add key and new value to dictionary
      v_dict[key] = new_val

    return v_dict

  def __calc_dot(self, probas: list, value: int) -> list:
    """Private helper function used to combine the dot product of a list of probabilities with a value."""
    return np.dot(probas, value)

class RandomPolicy(Policy):
  """A basic representation of a random policy."""
  def __init__(self, env: gym.Env) -> None:
    self.env = env
    self.state_space = env.observation_space
    self.action_space = env.action_space
    self.policy = {}

  def set_policy(self) -> dict:
    """Sets an evenly distributed probability for each action in all states. Returns it as a dictionary."""
    for state in range(self.state_space[1].n):
      probas = {}
      for action in range(self.action_space.n):
        # Set even probabilities based on actions
        probas[action] = 1 / self.action_space.n

        # Store probabilities for each state
        self.policy[state] = probas
    return self.policy
