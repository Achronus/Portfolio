class Vertex:
  """
  A type of node used within undirected graphs that use an adjacency matrix. Contains a name (object).
  """
  def __init__(self, name):
    self.name = name

class UDGraphMatrix:
  """
  An undirected graph data structure that uses a dictionary to store vertices in the format: name, object; edges within a 2D list; 
  and edge indices within a dictionary in the format: name, list index. The 2D list acts as an adjacency matrix that stores a 
  2D array of neighbours centered around a vertex.
  """
  def __init__(self):
    self.vertices = dict()
    self.edges = list()
    self.edge_indices = dict()
  
  def add_vertex(self, vertex):
    """
    Adds a vertex to the graph.

    Example:
      g = UDGraphMatrix()
      a = Vertex('A')
      g.add_vertex(a)
      g.add_vertex(Vertex('B'))

      for i in range(ord('A'), ord('K')):
        g.add_vertex(Vertex(chr(i)))
    """
    if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
      self.vertices[vertex.name] = vertex

      # Add column of zeros to edge matrix
      for row in self.edges:
        row.append(0)
      
      # Add row of zeros to bottom of edges matrix
      self.edges.append([0] * (len(self.edges) + 1))
      self.edge_indices[vertex.name] = len(self.edge_indices)
      return True
    else:
      return False
    
  def add_edge(self, v1, v2, weight=1):
    """
    Adds an edge to the graph. Takes in two vertices that connect to each other.

    Example:
      g = UDGraphMatrix()
      g.add_edge('A', 'B')

      edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'IH']
      for edge in edges:
        g.add_edge(edge[0], edge[1]) # first letter, second letter
    """
    if v1 in self.vertices and v2 in self.vertices:
      self.edges[self.edge_indices[v1]][self.edge_indices[v2]] = weight
      self.edges[self.edge_indices[v2]][self.edge_indices[v1]] = weight
      return True
    else:
      return False

  def print_graph(self):
    """
    Displays the graphs vertices and edges in sorted order.
    """
    key_len = len(next(iter(self.edge_indices)))
    # Top row
    print(' ' * key_len + ' | ', end='')
    for vertex, _ in sorted(self.edge_indices.items()):
      print(vertex + ' ', end='')
    print()

    # Matrix values
    for vertex, row in sorted(self.edge_indices.items()):
      print(vertex + ' | ', end='')
      for col in range(len(self.edges)):
        print(self.edges[row][col], end=' ')
      print(' ')