class Vertex:
  """
  A type of node used within undirected graphs that use an adjacency list. Contains a name (object) and a set of neighbours.
  """
  def __init__(self, name):
    self.name = name
    self.neighbours = set()
  
  def add_neighbour(self, vertex):
    """
    Adds a neighbour to the vertex.
    """
    self.neighbours.add(vertex)

class UDGraphList:
  """
  An undirected graph data structure that uses a dictionary to store vertices in the format: name, object. 
  The dictionary acts as an adjacency list that stores a list of neighbours in each vertex.
  """
  def __init__(self):
    self.vertices = dict()

  def add_vertex(self, vertex):
    """
    Adds a vertex to the graph.

    Example:
      g = UDGraphList()
      a = LUDVertex('A')
      g.add_vertex(a)
      g.add_vertex(Vertex('B'))

      for i in range(ord('A'), ord('K')):
        g.add_vertex(Vertex(chr(i)))
    """
    if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
      self.vertices[vertex.name] = vertex
      return True
    else:
      return False
  
  def add_edge(self, v1, v2):
    """
    Adds an edge to the graph. Takes in two vertices that connect to each other.

    Example:
      g = UDGraphList()
      g.add_edge('A', 'B')

      edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'IH']
      for edge in edges:
        g.add_edge(edge[0], edge[1]) # first letter, second letter
    """
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add_neighbour(v2)
      self.vertices[v2].add_neighbour(v1)
      return True
    else:
      return False
  
  def print_graph(self):
    """
    Displays the graphs vertices and edges in sorted order.
    """
    for key in sorted(list(self.vertices.keys())):
      print(key, sorted(list(self.vertices[key].neighbours)))

