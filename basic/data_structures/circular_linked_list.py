from parent._linked import Node, Linked

class CircularLinkedlist(Linked):
  """
  A variant of linked list, where the first element points to the last element and the last element points to the first element.
  """
  def __init__(self, root=None):
    super().__init__(root)

  def add(self, item):
    """
    Adds an item to the list.
    """
    if self.size == 0:
      self.root = Node(item)
      self.root.next_node = self.root
    else:
      new_node = Node(item, self.root.next_node)
      self.root.next_node = new_node
    
    self.size += 1

  def find(self, item):
    """
    Returns the position of a given item in the list.
    """
    this_node = self.root

    while True:
      # Node found
      if this_node.data == item:
        return True
      # Exit before looping over list again
      elif this_node.next_node == self.root:
        return False
      else:
        this_node = this_node.next_node

  def remove(self, item):
    """
    Removes an item from the list.
    """
    this_node = self.root
    prev_node = None

    while True:
      # Found data
      if this_node.data == item:
        if prev_node is not None:
          # Not a root node
          prev_node.next_node = this_node.next_node
        else:
          # Update last nodes next node position
          while this_node.next_node != self.root:
            this_node = this_node.next_node

          # Update root node
          this_node.next_node = self.root.next_node
          self.root = this_node.next_node
        
        # Data removed
        self.size -= 1
        return True
    
      # Exit before looping over list again
      elif this_node.next_node == self.root:
        return False
      
      # If not yet found, go to next node
      prev_node = this_node
      this_node = this_node.next_node

  def _print_condition(self, node):
    """
    Returns a unique print condition used within the print_list function.
    """
    return node.next_node != self.root