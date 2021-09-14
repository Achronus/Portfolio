from abc import ABC, abstractmethod

from mpl_toolkits.axes_grid1 import make_axes_locatable

from plotting.dataclasses import *

class Plot(ABC):
  """A template class for plots."""
  @abstractmethod
  def __init__(self) -> None:
    pass

  @abstractmethod
  def create_plots(self) -> None:
    pass

  @abstractmethod
  def _set_figure(self) -> None:
    pass

class MultiUsePlot(Plot):
  """A basic representation of a multi-use plot."""
  def __init__(self, text: FigureText, axis_data: AxisData,
               Z_data: ZCoordinateData, 
               surface_params: SurfaceParameters) -> None:
    self.text = text
    self.axis_data = axis_data
    self.z_data = Z_data
    self.surface_params = surface_params
  
  def create_plots(self, figsize: tuple, projection: str = None) -> None:
    """Creates two plots in one figure."""
    fig = plt.figure(figsize=figsize)

    # Set Usable Ace plot
    ax = fig.add_subplot(121, projection=projection)
    ax.set_title('Usable Ace')
    self._set_figure(True, ax)
    
    # Set No Usable Ace plot
    ax = fig.add_subplot(122, projection=projection)
    ax.set_title('No Usable Ace')
    self._set_figure(False, ax)
    plt.show()

  def _set_figure(self) -> None:
    pass

  def _get_Z(self, x: int, y: int, usable_ace: int, iterator: list, val: int) -> int:
    """Protected helper function used to get a Z coordinator. Returns an integer."""
    if (x, y, usable_ace) in iterator:
      return iterator[x, y, usable_ace]
    else:
      return val

  def _flatten(self, data: np.ndarray) -> np.ndarray:
    """Protected helper function that flattens a given numpy array and returns it."""
    return np.ravel(data)

  def _set_labels(self, ax: plt.axes, three_dims: bool = False) -> None:
    """Protected helper function used to set a plot labels."""
    ax.set_xlabel(self.text.x_label)
    ax.set_ylabel(self.text.y_label)
    
    if three_dims:
      ax.set_zlabel(self.text.z_label)

class PlotBlackjackValues(MultiUsePlot):
  """A 3D plot for blackjack values."""
  def __init__(self, text: FigureText, axis_data: AxisData,
               Z_data: ZCoordinateData, 
               surface_params: SurfaceParameters) -> None:
    super().__init__(text, axis_data, Z_data, surface_params)

  def _set_figure(self, usable_ace: bool, ax: plt.axes) -> None:
    """Protected helper function used to set a 3D figure."""
    Z = np.array([
      self._get_Z(x, y, usable_ace, self.z_data.iterator, self.z_data.return_val) 
      for x, y in zip(
        self._flatten(self.axis_data.X), 
        self._flatten(self.axis_data.Y)
      )
    ]).reshape(self.axis_data.X.shape)
    params_dict = dict((k, v) for k, v in self.surface_params.__dict__.items() if v != None)
    surf = ax.plot_surface(self.axis_data.X, self.axis_data.Y, Z, **params_dict)
    self._set_labels(ax, three_dims=True)
    ax.view_init(ax.elev, -120)

class PlotPolicy(MultiUsePlot):
  """A 2D plot for displaying the policy values."""
  def __init__(self, text: FigureText, axis_data: AxisData,
                Z_data: ZCoordinateData, 
                surface_params: SurfaceParameters) -> None:
    super().__init__(text, axis_data, Z_data, surface_params)

  def _set_figure(self, usable_ace: bool, ax: plt.axes) -> None:
    """Protected helper function used to set a 2D figure."""
    Z = np.array([
      [self._get_Z(x, y, usable_ace, self.z_data.iterator, self.z_data.return_val) for x in self.axis_data.x_range] for y in self.axis_data.y_range
    ])
    params_dict = dict((k, v) for k, v in self.surface_params.__dict__.items() if v != None)
    surf = ax.imshow(Z, **params_dict)
    plt.xticks(self.axis_data.x_range)
    plt.xticks(self.axis_data.y_range)
    plt.gca().invert_yaxis()
    self._set_labels(ax)
    ax.grid(color='w', linestyle='-', linewidth=1)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    cbar = plt.colorbar(surf, ticks=[0, 1], cax=cax)
    cbar.ax.set_yticklabels('0 (STICK)', '1 (HIT)')
