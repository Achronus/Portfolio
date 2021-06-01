#-----------------------------------------------------------------------
# File Title: Rectangle Class
# File Description: Handles all functionality for rectangles. 
#-----------------------------------------------------------------------
from .shape import Shape
from utils.movable import Movable

class Rectangle(Shape, Movable):
  """
  Handles all functionality for creating rectangles.\n
  Functions: (6) _calculate_area(), _calculate_perimeter(), _calculate_points(), display_stats(), move(new_x, new_y), scale(scale_x, scale_y)
  """
  def __init__(self, x=0, y=0, height=0, width=0):
    """
    Initalizes all rectangle variables.\n
    Variables: (2) height, width
    """
    Shape.__init__(self, x, y)
    self._x = x
    self._y = y
    self._height = height
    self._width = width

    # Calcluate all points
    self._calculate_points()

  def _calculate_area(self):
    """
    Used to calculate the area of the rectangle.
    """
    self._area = self._width * self._height

  def _calculate_perimeter(self):
    """
    Used to calculate the perimeter of the rectangle.
    """
    self._perimeter = (self._width * 2) + (self._height * 2)

  def _calculate_points(self):
    """
    Used to calculate each point of the rectangle and stores them in a points list.
    """
    # left_top
    self._points.append(self._left_top)

    # right_top
    self._points.append(tuple((self._left_top[0] + self._width, self._left_top[1])))

    # right_bottom
    self._points.append(tuple((self._left_top[0] + self._width, self._left_top[1] + self._height)))

    # left_bottom
    self._points.append(tuple((self._left_top[0], self._left_top[1] + self._height)))

    # Calculate area and perimeter
    self._calculate_area()
    self._calculate_perimeter()

  def display_stats(self):
    """
    Displays the rectangle statistics to the screen.
    """
    print(f"Rectangle[h={self._height},w={self._width}]")
    print(f"Points{self._points}")
    print(f"Area={self._area:.2f} Perimeter={self._perimeter:.2f}")

  def move(self, new_x, new_y):
    """
    Moves the position of the rectangle to a new location by updating the left_top points and recalculates the other points.\n
    Parameters: (2) new x value, new y value
    """
    # Replace left_top values
    self._left_top = (new_x, new_y)

    # Reset and update points
    self._points.clear()
    self._calculate_points()

  def scale(self, scale_x, scale_y):
    """
    Scales a rectangles size to either be larger or smaller. Updates the left_top points and recalculates the other points.\n
    Parameters: (2) new scale x value, new scale y value
    """
    # Update width and height
    self._width *= scale_x
    self._height *= scale_y

    # Reset and update points
    self._points.clear()
    self._calculate_points()