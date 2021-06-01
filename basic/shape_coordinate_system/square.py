#-----------------------------------------------------------------------
# File Title: Square Class
# File Description: Handles all functionality for squares. 
#-----------------------------------------------------------------------
from shape import Shape
from movable import Movable

#-----------------------------------------------------------------------
# Num: 1 | Title: Square()
#-----------------------------------------------------------------------
class Square(Shape, Movable):
  """
  Handles all functionality for creating squares.\n
  Functions: (6) _calculate_area(), _calculate_perimeter(), _calculate_points(), display_stats(), move(new_x, new_y), scale(scale_x, scale_y)
  """
  #-----------------------------------------------------------------------
  # Num: a | Title: __init__()
  #-----------------------------------------------------------------------
  def __init__(self, x=0, y=0, edges=0):
    """
    Initalizes all square variables.\n
    Variables: (1) edges
    """
    Shape.__init__(self, x, y)
    self._x = x
    self._y = y
    self._edges = edges

    # Calculate all points
    self._calculate_points()

  #-----------------------------------------------------------------------
  # Num: b | Title: _calculate_area()
  #-----------------------------------------------------------------------
  def _calculate_area(self):
    """
    Used to calculate the area of the square.
    """
    self._area = self._edges ** 2

  #-----------------------------------------------------------------------
  # Num: c | Title: _calculate_perimeter()
  #-----------------------------------------------------------------------
  def _calculate_perimeter(self):
    """
    Used to calculate the perimeter of the square.
    """
    self._perimeter = self._edges * 4

  #-----------------------------------------------------------------------
  # Num: d | Title: _calculate_points()
  #-----------------------------------------------------------------------
  def _calculate_points(self):
    """
    Used to calculate each point of the square and stores them in a points list.
    """
    # left_top
    self._points.append(self._left_top)

    # right_top
    self._points.append(tuple((self._left_top[0] + self._edges, self._left_top[1])))

    # right_bottom
    self._points.append(tuple((self._left_top[0] + self._edges, self._left_top[1] + self._edges)))

    # left_bottom
    self._points.append(tuple((self._left_top[0], self._left_top[1] + self._edges)))

    # Calculate area and perimeter
    self._calculate_area()
    self._calculate_perimeter()

  #-----------------------------------------------------------------------
  # Num: e | Title: display_stats()
  #-----------------------------------------------------------------------
  def display_stats(self):
    """
    Displays the squares statistics to the screen.
    """
    print(f"Square[e={self._edges}]")
    print(f"Points{self._points}")
    print(f"Area={self._area:.2f} Perimeter={self._perimeter:.2f}")

  #-----------------------------------------------------------------------
  # Num: f | Title: move()
  #-----------------------------------------------------------------------
  def move(self, new_x, new_y):
    """
    Moves the position of the square to a new location by updating the left_top points and recalculates the other points.\n
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
    Scales a squares size to either be larger or smaller. Updates the left_top points and recalculates the other points.\n
    Parameters: (2) new scale x value, new scale y value
    """
    # Check if scale values are same
    if (scale_x != scale_y):
      print("Scale amounts must be the same! Squares are strictly isotropic.")
    else:
      # Update radius
      self._edges *= scale_x
    
      # Reset and update points
      self._points.clear()
      self._calculate_points()