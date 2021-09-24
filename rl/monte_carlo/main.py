"""
Uses a Blackjack environment based on the card game. The goal of the 
game is to obtain cards that sum to as near as possible to 21 without going over.  

In this version the player is playing against a fixed dealer, where:
 - Face cards (Jack, Queen, King) have the point value of 10
 - Aces can either count as 11 or 1, and is called 'usable' at 11
 - The game uses an infinite deck (with card replacements)
 - The game starts with the player and dealer having one face up and one face down card

The player has two actions, hit and stick, where:
 - STICK = 0: keep the hand they currently have and move to dealers turn
 - HIT = 1: request additional cards until they decide to stop

The player busts if they exceed 21 (loses). After the player sticks, the dealer reveals 
their facedown card, and draws until their sum is 17 or greater. If the dealer goes 
bust the player wins.

If neither the player nor the dealer busts, the outcome (win, lose, draw) is
decided by whose sum is closest to 21. 

Reward scores:
 - Win = +1
 - Draw = 0
 - Lose = -1

The observation of the environment is a tuple of 3 items: 
 - The players current sum (0, 1, ..., 31)
 - The dealer's one showing card (1, ..., 10)
 - An indicator that determines the player holding a usable ace (no=0, yes=1)
"""
import gym
import numpy as np

from mc.prediction import MCPrediction
from utils.policy import LimitedPolicy
from utils.episodes import GenerateLimitedEpisodes
from plotting.dataclasses import FigureText
from plotting.plotter import Plotter

NUM_EPISODES = 500000
GAMMA = 1.0

ENV: gym.Env = gym.make('Blackjack-v1')
POLICY = LimitedPolicy()
EPISODE_TYPE = GenerateLimitedEpisodes(env=ENV, policy=POLICY)
MC = MCPrediction(env=ENV, episode_type=EPISODE_TYPE, gamma=GAMMA)

def plot_data(Q: tuple, policy: tuple) -> None:
  """Creates a 3D visualisation for the Q-value function and a 2D visualisation of the policy values."""
  # Format data
  Q_fv = POLICY.Q_to_plot(Q[0])

  # Set plotters
  fv_plotter = Plotter(Q_fv)
  text = FigureText("Player's Current Sum", "Dealer's Showing Card", "State Value")

  # Plot blackjack values (prediction)
  fv_plotter.plot_blackjack_values(
    text=text,
    x_range=np.arange(11, 22),
    y_range=np.arange(1, 11),
    figsize=(10, 10)
  )

  # Plot policy values (control)
  # for plot_class in [fv_plotter, ev_plotter]:
  #   plot_class.plot_policy(
  #     text=text,
  #     x_range=np.arange(11, 22),
  #     y_range=np.arange(10, 0, -1),
  #     figsize=(15, 15)
  #   )

def main() -> None:
  """Runs the main functionality of the game."""
  # Perform first-visit MC Prediction
  Q_fv, time_fv = MC.predict(MC.first_visit, NUM_EPISODES)
  print(f"\nFirst-visit: {time_fv:.4g} seconds")

  # Perform every-visit MC Prediction
  Q_ev, time_ev = MC.predict(MC.every_visit, NUM_EPISODES)
  print(f"\nEvery_visit: {time_ev:.4f} seconds")

  # Visualise Q-value functions and policies
  plot_data(Q=(Q_fv, Q_ev), policy=())

# Run main functionality
if __name__ == "__main__":
  main()
