"""
Uses the FrozenLake Gym environment outlined as:
  SFFF
  FHFH
  FFFH
  HFFG

  S : starting point, safe
  F : frozen surface, safe
  H : hole, fall to your doom
  G : goal, where the frisbee is located

In matrix format with state numbers:
  [[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]
  [12 13 14 15]]

The agent has four potential actions:
  LEFT = 0
  DOWN = 1
  RIGHT = 2
  UP = 3
"""
import gym
import time
import numpy as np

from iterate import ValueIteration

def main() -> None:
  """Runs the main functionality of the game."""
  env = gym.make('FrozenLake-v0')
  policy = np.ones([env.nS, env.nA]) / env.nA # random policy
  policy_type = ValueIteration(env=env)

  start_time = time.time()
  policy_pi, V_pi = policy_type.iterate(policy)
  end_time = time.time()
  print("Optimal Policy (LEFT = 0, DOWN = 1, RIGHT = 2, UP = 3):\n",policy_pi)
  print("\nOptimal State-Value Function:\n",V_pi)
  print(f"Time taken: {end_time - start_time:.4f} seconds")

# Run main functionality
if __name__ == "__main__":
  main()
