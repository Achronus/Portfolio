class OrderedContainer:
  """
  A template container that can be inherited from.
  """
  def __init__(self):
    self.container = list()

  def push_back(self, item):
    """
    Adds an item to the top of the container.
    """
    self.container.append(item)
  
  def empty(self):
    """
    Empties the container.
    """
    if len(self.container) > 0:
      self.container.clear()
    else:
      return None

  def size(self):
    """
    Returns the size of the container.
    """
    return len(self.container)

  def __str__(self):
    return str(self.container)