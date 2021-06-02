from parent._linked import Node, Linked

class DoublyLinkedList(Linked):
  """
  A variant of linked list, where each node has two links. The first link points to the previous node and the second link to the next node.
  """
  def __init__(self, root=None):
    super().__init__(root)
    self.last = root

  def add(self, item):
    """
    Adds an item to the list.
    """
    if self.size == 0:
      self.root = Node(item)
      self.last = self.root
    else:
      new_node = Node(item, self.root)
      self.root.prev_node = new_node
      self.root = new_node
    
    self.size += 1
  
  def remove(self, item):
    """
    Removes an item from the list.
    """
    this_node = self.root

    while this_node is not None:
      if this_node.data == item:
        if this_node.prev_node is not None:
          # Delete a middle node
          if this_node.next_node is not None:
            this_node.prev_node.next_node = this_node.next_node
            this_node.next_node.prev_node = this_node.prev_node
          # Delete last node
          else:
            this_node.prev_node.next_node = None
            self.last = this_node.prev_node
        
        # Delete root node
        else:
          self.root = this_node.next_node
          this_node.next_node.prev_node = self.root
        
        # Data removed
        self.size -= 1
        return True
      
      # Check the next node
      else:
        this_node = this_node.next_node
    
    # Data not found
    return False

  def _print_condition(self, node):
    """
    Returns a unique print condition used within the print_list function.
    """
    return node.next_node is not None