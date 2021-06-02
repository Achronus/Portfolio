from parent._container import OrderedContainer

class Queue(OrderedContainer):
  """
  First-in first-out (FIFO) data structure, where elements are inserted to one end of the container and removed from the other.
  """
  def __init__(self):
    super().__init__()
    self.queue = self.container

  def pop_front(self):
    """
    Removes the bottom item from the queue.
    """
    if len(self.queue) > 0:
      del self.queue[0]
    else:
      return None

  def front(self):
    """
    Checks the bottom item of the queue.
    """
    if len(self.queue) > 0:
      return self.queue[0]
    else:
      return None

  def back(self):
    """
    Checks the top item of the queue.
    """
    if len(self.queue) > 0:
      return self.queue[len(self.queue)-1]
    else:
      return None