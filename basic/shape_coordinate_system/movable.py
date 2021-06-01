#-----------------------------------------------------------------------
# File Title: Movable Class
# File Description: Abstract class for the shape class. 
#-----------------------------------------------------------------------
from abc import ABC, abstractmethod

#-----------------------------------------------------------------------
# Num: 1 | Title: Movable()
#-----------------------------------------------------------------------
class Movable(ABC):
  """
  An abstract class used for the shape class, enables move and scale functionalty for child shape classes.\n
  Functions: (2) move(new_x, new_y), scale(scale_x, scale_y)
  """
  #-----------------------------------------------------------------------
  # Num: a | Title: move()
  #-----------------------------------------------------------------------
  @abstractmethod
  def move(self, new_x, new_y):
    """
    Moves the position of the shape to a new location by updating the left_top points and recalculates the other points.\n
    Parameters: (2) new x value, new y value
    """
    pass

  #-----------------------------------------------------------------------
  # Num: b | Title: scale()
  #-----------------------------------------------------------------------
  @abstractmethod
  def scale(self, scale_x, scale_y):
    """
    Scales a shapes size to either be larger or smaller. Updates the left_top points and recalculates the other points.\n
    Parameters: (2) new scale x value, new scale y value
    """
    pass