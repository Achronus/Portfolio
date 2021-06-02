from parent._container import OrderedContainer

class Stack(OrderedContainer):
  """
  Last-in first-out (LIFO) data structure, where elements are inserted and extracted only from one end of the container.
  """
  def __init__(self):
    super().__init__()
    self.stack = self.container

  def pop_back(self):
    """
    Removes the top item from the stack.
    """
    if len(self.stack) > 0:
      return self.stack.pop()
    else:
      return None

  def peek(self):
    """
    Checks the top item of the stack.
    """
    if len(self.stack) > 0:
      return self.stack[len(self.stack)-1]
    else:
      return None