class Heap:
  """
  A template of a binary tree that can be inherited from.
  """
  def __init__(self, items=None):
    self.heap = []

    if items is not None:
      self.heapify(items)

  def push(self, item):
    """
    Adds a new value to the heap.
    """
    self.heap.append(item)
    self._siftdown(0, self.size() - 1)

  def peek(self):
    """
    Returns the top value (root node) in the heap.
    """
    if self.heap[0]:
      return self.heap[0]
    else:
      return None

  def pop(self):
    """
    Removes the top value (root node) from the heap.
    """
    if self.size() > 1:
      self._swap(0, self.size() - 1) # swap first and last items
      max_value = self.heap.pop() # remove last item
      self._siftup(0) # reposition first item

    # One item in heap
    elif self.size() == 1:
      max_value = self.heap.pop()
    
    # Heap is empty
    else:
      max_value = None

    return max_value

  def heapify(self, data):
    """
    Transform a list into a heap, in-place, in O(len(n)) time.
    """
    n = len(data)
    for i in reversed(range(n//2)):
      self._siftup(i, data)

  def _swap(self, i, j):
    """
    Swap the location of two items in the heap.
    """
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def replace(self, item):
    """
    Replaces an item on the heap.
    """
    if self.size() > 1:
      r_item, self.heap[0] = self.heap[0], item
      self._siftup(0)
      return r_item
    else:
      return None

  def _siftup(self, position):
    """
    Moves an item up the heap to its correct location.
    """
    pass

  def _siftdown(self, start_position, position):
    """
    Moves an item down the heap to its correct location.
    """
    pass
  
  def size(self):
    """
    Returns the size of the heap.
    """
    return len(self.heap)

  def left_child(self, position):
    """
    Returns the position of the left child at the given value.
    """
    return 2 * position

  def right_child(self, position):
    """
    Returns the position of the right child at the given value.
    """
    return (2 * position) + 1
  
  def __str__(self):
    return str(self.heap)