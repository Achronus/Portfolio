from parent._heap import Heap

class MaxHeap(Heap):
  """
  A binary tree that uses the maximum value at the root of its tree.
  """
  def __init__(self, items=None):
    super().__init__(items)

  def _siftup(self, position, data=None):
    """
    Moves an item up the heap to its correct location.
    """
    if data is not None:
      self.heap = data

    end_position = len(self.heap)
    start_position = len(self.heap)
    new_item = self.heap[position]

    # Bubble up the larger child until reached a leaf
    child_position = self.left_child(position)

    while child_position < end_position:
      right_position = self.right_child(position)
      
      # Set child to index of smaller child
      if right_position < end_position and not self.heap[child_position] > self.heap[right_position]:
        child_position = right_position
      
      # Move the larger child up
      self.heap[position] = self.heap[child_position]
      position = child_position
      child_position = self.right_child(position)

    # Bubble up new item to final place (shift parent down)
    self.heap[position] = new_item
    self._siftdown(start_position, position)

  def _siftdown(self, start_position, position):
    """
    Moves an item down the heap to its correct location.
    """
    new_item = self.heap[position]

    while position > start_position:
      parent_position = (position - 1) >> 1
      parent = self.heap[parent_position]

      # Compare items
      if new_item > parent:
        self.heap[position] = parent
        position = parent_position
        continue
      break
    
    self.heap[position] = new_item