#---------------------------------------------------------------------------
# File Title: Point Class
# File Description: Used to represent a location in the coordinate system. 
#---------------------------------------------------------------------------
class Point():
  """
  Used to represent a location in the coordinate system using the variables: x, y.\n
  Only contains a constructor to initalize the x and y values.
  """
  def __init__(self, x=0, y=0):
    """
    Initalizes x and y variables.
    """
    self._x = x
    self._y = y