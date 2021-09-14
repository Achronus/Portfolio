from plotting.dataclasses import *
from plotting.plots import PlotBlackjackValues, PlotPolicy

class Plotter:
  """Handles the functionality for plotting the environments activity."""
  def __init__(self, Q: dict = {}, policy: dict = {}) -> None:
    self.Q = Q # estimated value function
    self.policy = policy

  def plot_blackjack_values(self, text: FigureText, x_range: np.ndarray, y_range: np.ndarray, figsize: tuple) -> None:
    """Plots a 3D representation of the blackjack values."""
    # Set data items
    axis_data = AxisData(
      x_range=x_range,
      y_range=y_range,
      x_y_mesh=np.meshgrid(x_range, y_range)
    )
    surface_params = SurfaceParameters(
      cmap=plt.cm.coolwarm,
      vmin=-1.0,
      vmax=1.0,
      rstride=1,
      cstride=1
    )
    z_data = ZCoordinateData(self.Q, 0)
    graph = PlotBlackjackValues(text, axis_data, z_data, surface_params)
    graph.create_plots(figsize, projection='3d')

  def plot_policy(self, text: FigureText, x_range: np.ndarray, y_range: np.ndarray, figsize: tuple):
    """Plots a 2D representation of the policy values."""
    axis_data = AxisData(
      x_range=x_range,
      y_range=y_range,
      x_y_mesh=np.meshgrid(x_range, y_range)
    )
    surface_params = SurfaceParameters(
      cmap=plt.get_cmap('Pastel2', 2),
      vmin=0,
      vmax=1,
      extent=[10.5, 21.5, 0.5, 10.5]
    )
    z_data = ZCoordinateData(self.policy, 1)
    graph = PlotPolicy(text, axis_data, z_data, surface_params)
    graph.create_plots(figsize)
