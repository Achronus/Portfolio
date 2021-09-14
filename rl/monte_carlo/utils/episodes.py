from abc import ABC, abstractmethod

import gym
import numpy as np

from utils.policy import Policy

class Episode(ABC):
  """A template class for episodes."""
  @abstractmethod
  def __init__(self) -> None:
    pass

  @abstractmethod
  def get_episode(self) -> None:
    pass

class GenerateLimitedEpisodes(Episode):
  """
  Generates a set of episodes from the environment. The episodes generated are limited to a specific sequence of probabilities. If the players cards exceed the sum of 18, there is an 80% chance they will STICK. If the sum is below 18, there is an 80% chance they will HIT.
  """
  def __init__(self, env: gym.Env, policy: Policy) -> None:
    self.env = env
    self.policy = policy

  def get_episode(self) -> list:
    """Used to retrieve an episode from the environment, returned as a list of tuples: [(state, action, reward)]."""
    episode: list = []
    state: int = self.env.reset() # player score

    while True:
      probas = self.policy.set_policy(state)
      action = np.random.choice(np.arange(2), p=probas) # select a random action with a set probability
      next_state, reward, done, _ = self.env.step(action)
      episode.append((state, action, reward)) # store episode results

      # Update state
      state = next_state

      # Check for episode completion
      if done:
        break

    return episode
