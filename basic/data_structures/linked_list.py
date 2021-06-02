from parent._linked import Node, Linked

class LinkedList(Linked):
  """
  A linear data structure, in which the elements are not stored at contiguous memory locations. 
  Instead, the elements are linked using pointers in the form of nodes.
  """
  def __init__(self, root=None):
    super().__init__(root)

  def add(self, item):
    """
    Adds an item to the list.
    """
    new_node = Node(item, self.root)
    self.root = new_node
    self.size += 1

  def remove(self, item):
    """
    Removes an item from the list.
    """
    this_node = self.root
    prev_node = None

    while this_node is not None:
      if this_node.data == item:
        if prev_node is not None:
          # Not a root node
          prev_node.next_node = this_node.next_node
        else:
          # Is a root node
          self.root = this_node.next_node
        
        # Data removed
        self.size -= 1
        return True
    
      else:
        # If not yet found, go to next node
        prev_node = this_node
        this_node = this_node.next_node
    
    # data not found
    return False

  def print_list(self):
    """
    Displays the list contents.
    """
    this_node = self.root

    while this_node is not None:
      this_node = this_node.next_node
      print(this_node, end='->')
    print('None')