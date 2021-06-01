#-----------------------------------------------------------------------
# File Title: Shape Class
# File Description: Abstract class for the shape class. 
#-----------------------------------------------------------------------
from abc import ABC, abstractmethod
from utils.point import Point

class Shape(ABC):
  """
  Abstract class for all child shapes. Contains a constructor and four functions.\n
  Functions: (4) calculate_area(), calculate_perimeter(), calculate_points(), display_stats()
  """
  def __init__(self, x=0, y=0, left_top=(0, 0), area=0, perimeter=0, points=[]):
    """
    Initalizes all shape variables.\n
    Variables: (6)
      1. x - inherited from Point class
      2. y - inherited from Point class
      3. left_top - (x, y) coordinates
      4. area - area calculation of the shape
      5. perimeter - perimeter calculation of the shape
      6. points - tuple of point locations (up to 4 sets of points)
    """
    Point.__init__(self, x, y)
    self._left_top = (x, y)
    self._area = area
    self._perimeter = perimeter
    self._points = list(points)

  @abstractmethod
  def _calculate_area(self):
    """
    Used to calculate the area of the shapes.
    """
    pass

  @abstractmethod
  def _calculate_perimeter(self):
    """
    Used to calculate the perimeter of the shapes.
    """
    pass

  @abstractmethod
  def _calculate_points(self):
    """
    Used to calculate each location of the shapes and stores them in a points list.
    """
    pass

  @abstractmethod
  def display_stats(self):
    """
    Displays the shape statistics to the screen.
    """
    pass