class BinaryTree:
  """
  A binary tree.
  """
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def insert(self, item):
    """
    Adds a node to the tree.
    """
    # Duplicate value
    if self.data == item:
      return False
    
    # Add to the left branch
    elif self.data > item:
      if self.left is not None:
        return self.left.insert(item)
      else:
        # Create new sub-tree
        self.left = BinaryTree(item)
        return True
    
    # Add to the right branch
    else:
      if self.right is not None:
        return self.right.insert(item)
      else:
        # Create new sub-tree
        self.right = BinaryTree(item)
        return True

  def find(self, item):
    """
    Used to find a node within the tree.
    """
    # Item found
    if self.data == item:
      return item
    
    # Search left
    elif self.data > item:
      if self.left is None:
        return False
      else:
        return self.left.find(item)
    
    # Search right
    else:
      if self.right is None:
        return False # Not found
      else:
        return self.right.find(item)

  def get_size(self):
    """
    Returns the size of the tree.
    """
    if self.left is not None and self.right is not None:
      return 1 + self.left.get_size() + self.right.get_size()
    elif self.left:
      return 1 + self.left.get_size()
    elif self.right:
      return 1 + self.right.get_size()
    else:
      return 1

  def traverse(self, type='preorder'):
    """
    Output the tree in the given type order. Type orders are: preorder or inorder.
    """
    # Perform required traversal
    if type == 'preorder':
      self._preorder()
    elif type == 'inorder':
      self._inorder()

  def _preorder(self):
    """
    Helper function used in traverse. Performs preorder traversal, 
    where the root node is visted before its subtrees.
    """
    if self is not None:
      print(self.data, end=' ')
      if self.left is not None:
        self.left._preorder()
      if self.right is not None:
        self.right._preorder()

  def _inorder(self):
    """
    Helper function used in traverse. Performs inorder traversal, 
    where the root node is visted between the root nodes subtrees.
    Reads and returns values in sorted order. 
    """
    if self is not None:
      if self.left is not None:
        self.left._inorder()
      print(self.data, end=' ')
      if self.right is not None:
        self.right._inorder()

  def remove(self, item):
    """
    Deletes a node from the tree.
    """
    # Empty tree
    if self is None:
      return False

    # Item is in root node
    elif self.data == item:
      if self.left is None and self.right is None:
        self.data = None
      elif self.left and self.right is None:
        self.data = self.left
      elif self.left is None and self.right:
        self.data = self.right
      elif self.left and self.right:
        delete_parent = self.data
        delete_node = self.right
        while delete_node.left:
          delete_parent = delete_node
          delete_node = delete_node.left
        
        self.data = delete_node.data
        if delete_node.right:
          if delete_parent.data > delete_node.data:
            delete_parent.left = delete_node.right
          elif delete_parent.data < delete_node.data:
            delete_parent.right = delete_node.right
        else:
          if delete_node.data < delete_parent.data:
            delete_node.left = None
          else:
            delete_parent.right = None
      return True
      
    parent = None
    node = self
    # Find node to remove
    while node.data and node.data != item:
      parent = node
      if item < node.data:
        node = node.left
      elif item > node.data:
        node = node.right
    
    # Case 1: data not found
    if node.data is None or node.data != item:
      return False
    
    # Case 2: remove-node has no children
    elif node.left is None and node.right is None:
      if item < parent.data:
        parent.left = None
      else:
        parent.right = None
      return True
    
    # Case 3: remove-node has left child only
    elif node.left and node.right is None:
      if item < parent.data:
        parent.left = node.left
      else:
        parent.right = node.left
      return True
    
    # Case 4: remove-node has right child only
    elif node.left is None and node.right:
      if item < parent.data:
        parent.left = node.right
      else:
        parent.right = node.right
      return True
    
    # Case 5: remove-node has left and right children
    else:
      delete_parent = node
      delete_node = node.right
      while delete_node.left:
        delete_parent = delete_node
        delete_node = delete_node.left
      
      node.data = delete_node.data
      if delete_node.right:
        if delete_parent.data > delete_node.data:
          delete_parent.left = delete_node.right
        elif delete_parent.data < delete_node.data:
          delete_parent.right = delete_node.right
      else:
        if delete_node.data < delete_parent.data:
          delete_parent.left = None
        else:
          delete_parent.right = None
      return True
