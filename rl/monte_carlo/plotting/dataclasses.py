from dataclasses import dataclass
from collections import defaultdict

import gym
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class FigureText:
  """A data class that stores the label text for plots."""
  x_label: str
  y_label: str
  z_label: str

class AxisData:
  """A data class for storing the plots X and Y data."""
  def __init__(self, x_range: np.ndarray, y_range: np.ndarray, x_y_mesh: tuple) -> None:
    self.x_range = x_range
    self.y_range = y_range
    self.X = x_y_mesh[0]
    self.Y = x_y_mesh[1]

@dataclass
class ZCoordinateData:
  """A data class that stores the Z coordinate data."""
  iterator: list
  return_val: int

@dataclass
class SurfaceParameters:
  """A data class for storing plot surface parameters."""
  cmap: plt.cm
  vmin: float
  vmax: float
  rstride: int = None
  cstride: int = None
  extent: list = None

class MCDataDicts:
  """A data class used to store the MC Prediction dictionaries."""
  def __init__(self, env: gym.Env) -> None:
    self.return_sum = self.__initialize_dict(env.action_space.n) # sum of rewards after visit
    self.N = self.__initialize_dict(env.action_space.n) # visit count for each state-action pair
    self.Q = self.__initialize_dict(env.action_space.n) # Q-table for storing the average reward for each state-action pair

  def __initialize_dict(self, dimensions: int) -> dict:
    """Private helper function used to initialize and return a dictionary based on the given dimensions."""
    return defaultdict(lambda: np.zeros(dimensions)) 
