class Node:
  """
  A node that stores data passed in and optionally stores the next and previous nodes.
  """
  def __init__(self, data, next=None, prev=None):
    self.data = data
    self.next_node = next
    self.prev_node = prev # used for doubly linked lists

  def __str__(self):
    return "(" + str(self.data) + ")"

class Linked:
  """
  A linear data structure template, where the elements are linked using pointers in the form of nodes.
  """
  def __init__(self, root=None):
    self.root = root
    self.size = 0

  def find(self, item):
    """
    Returns the position of a given item in the list.
    """
    this_node = self.root

    while this_node is not None:
      # Node found
      if this_node.data == item:
        return True
      # Node not found
      elif this_node.next_node == None:
        return False
      # Check remaining nodes
      else:
        this_node = this_node.next_node

  def _print_condition(self, node):
    """
    Returns a unique print condition used within the print_list function.
    """
    pass

  def print_list(self):
    """
    Displays the list contents.
    """
    if self.root is None:
      return

    this_node = self.root
    print(this_node, end='->')

    # Stop when root node
    while self._print_condition(this_node):
      this_node = this_node.next_node
      print(this_node, end='->')
    print()