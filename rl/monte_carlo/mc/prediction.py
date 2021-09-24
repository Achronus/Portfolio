import time

from utils.episodes import Episode
from plotting.dataclasses import MCDataDicts

import gym
import numpy as np

def time_me(func: object) -> tuple:
  """Decorator for timing MC Prediction functions."""
  def wrapper(*args) -> tuple:
    start_time = time.perf_counter()
    Q = func(*args)
    time_taken = time.perf_counter() - start_time
    return Q, time_taken
  return wrapper

class MCPrediction:
  """A basic representation of Monte-Carlo Prediction."""
  def __init__(self, env: gym.Env, episode_type: Episode, gamma: float = 1.0) -> None:
    self.env = env
    self.episode_type = episode_type
    self.gamma = gamma

    self.dicts = MCDataDicts(env)

  def generate_episode(self) -> list:
    """Generates a single episode and returns it as an object that contains a list of tuples: [(states, actions, rewards)]."""
    return self.episode_type.get_episode()

  def first_visit(self, episode: list) -> None:
    """First-visit MC Prediction for an action-value function."""
    # Set states, actions, rewards and discounted return
    states, actions, rewards, G = self.__set_components(episode)

    for idx, state in enumerate(states):
      # Update dictionaries every first-visit
      if state not in states[:idx]:
        self.__update_dicts(state, actions, rewards, idx, G)

  def every_visit(self, episode: list) -> None:
    """Every-visit MC Prediction for an action-value function."""
    # Set states, actions, rewards and discounted return
    states, actions, rewards, G = self.__set_components(episode)

    for idx, state in enumerate(states):
      # Update dictionaries every visit
      self.__update_dicts(state, actions, rewards, idx, G)

  @time_me
  def predict(self, visit_func: object, num_episodes: int) -> np.ndarray:
    """Performs Monte-Carlo Prediction and returns an updated Q-table based on the given visit function - first_visit or every_visit."""
    # Loop over each episode
    for episode in range(num_episodes):
      # Monitor progress
      if episode % 1000 == 0:
        print(f"\r{visit_func.__name__} episode {episode}/{num_episodes}.", end="", flush=True)

      # Generate an episode
      episode = self.generate_episode()

      # Update dictionaries with Monte-Carlo prediction method
      visit_func(episode)

    # Return updated Q-table
    return self.dicts.Q

  def __set_components(self, episode: list) -> tuple:
    """Private helper function used to set the states, actions, rewards and discounted rewards. Returns them as a tuple."""
    S, A, R = zip(*episode) # Set states, actions, rewards
    G = np.array([self.gamma**r for r in range(len(R)+1)]) # Apply discounted return to rewards
    return S, A, R, G

  def __update_dicts(self, state: tuple, actions: tuple, rewards: tuple, idx: int, G: np.ndarray) -> None:
    """Private helper function used to update the dictionary values."""
    # return_sum - (([hand_total], [dealer_hand], [usable_ace]), 
    #               ([usable_ace_reward_total], [no_usable_ace_reward_total]))
    self.dicts.return_sum[state][actions[idx]] += sum(rewards[idx:] * G[:-(idx+1)])
    
    # N - (([hand_total], [dealer_hand], [usable_ace]), 
    #      ([usable_ace_count_total], [no_usable_ace_count_total]))
    self.dicts.N[state][actions[idx]] += 1.0 # counter

    # Q - (([hand_total], [dealer_hand], [usable_ace]), 
    #      ([usable_ace_average_reward], [no_usable_ace_average_reward]))
    error = self.dicts.return_sum[state][actions[idx]] - self.dicts.Q[state][actions[idx]]
    self.dicts.Q[state][actions[idx]] = error / self.dicts.N[state][actions[idx]]
