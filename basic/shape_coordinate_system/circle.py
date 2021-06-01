#-----------------------------------------------------------------------
# File Title: Circle Class
# File Description: Handles all functionality for circles. 
#-----------------------------------------------------------------------
from shape import Shape
from movable import Movable
from math import pi

#-----------------------------------------------------------------------
# Num: 1 | Title: Circle()
#-----------------------------------------------------------------------
class Circle(Shape, Movable):
  """
  Handles all functionality for creating circles.\n
  Functions: (6) _calculate_area(), _calculate_perimeter(), _calculate_points(), display_stats(), move(new_x, new_y), scale(scale_x, scale_y)
  """
  #-----------------------------------------------------------------------
  # Num: a | Title: __init__()
  #-----------------------------------------------------------------------
  def __init__(self, x=0, y=0, radius=0):
    """
    Initalizes all circle variables.\n
    Variables: (1) radius
    """
    Shape.__init__(self, x, y)
    self._x = x
    self._y = y
    self._radius = radius

    # Calculate all points
    self._calculate_points()

  #-----------------------------------------------------------------------
  # Num: b | Title: _calculate_area()
  #-----------------------------------------------------------------------
  def _calculate_area(self):
    """
    Used to calculate the area of circles.
    """
    self._area = pi * (self._radius**2)

  #-----------------------------------------------------------------------
  # Num: c | Title: _calculate_perimeter()
  #-----------------------------------------------------------------------
  def _calculate_perimeter(self):
    """
    Used to calculate the circumference of circles.
    """
    self._perimeter = pi * (2 * self._radius)

  #-----------------------------------------------------------------------
  # Num: d | Title: _calculate_points()
  #-----------------------------------------------------------------------
  def _calculate_points(self):
    """
    Used to calculate each location of circles created and stores them in a points list.
    """
    # left_top
    self._points.append(self._left_top)

    # right_bottom
    new_radius = 2 * self._radius
    self._points.append(tuple((self._left_top[0] + new_radius, self._left_top[1] + new_radius)))

    # Calculate area and perimeter
    self._calculate_area()
    self._calculate_perimeter()

  #-----------------------------------------------------------------------
  # Num: e | Title: display_stats()
  #-----------------------------------------------------------------------
  def display_stats(self):
    """
    Displays the circle statistics to the screen.
    """
    print(f"Circle[r={self._radius}]")
    print(f"Points{self._points}")
    print(f"Area={self._area:.2f} Perimeter={self._perimeter:.2f}")

  #-----------------------------------------------------------------------
  # Num: f | Title: move()
  #-----------------------------------------------------------------------
  def move(self, new_x, new_y):
    """
    Moves the position of the circle to a new location by updating the left_top points and recalculates the other points.\n
    Parameters: (2) new x value, new y value
    """
    # Replace left_top values
    self._left_top = (new_x, new_y)

    # Reset and update points
    self._points.clear()
    self._calculate_points()

  #-----------------------------------------------------------------------
  # Num: g | Title: scale()
  #-----------------------------------------------------------------------
  def scale(self, scale_x, scale_y):
    """
    Scales a circles size to either be larger or smaller. Updates the left_top points and recalculates the other points.\n
    Parameters: (2) new scale x value, new scale y value
    """
    # Check if scale values are same
    if (scale_x != scale_y):
      print("Scale amounts must be the same! Circles are strictly isotropic.")
    else:
      # Update radius
      self._radius *= scale_x
    
      # Reset and update points
      self._points.clear()
      self._calculate_points()