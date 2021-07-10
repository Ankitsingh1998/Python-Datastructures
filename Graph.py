#Data structure - Graph
class Graph: 
    def __init__(self, size): 
        self.adj = [ [0] * size for i in range(size)]
        self.size = size 
    
    def add_edge(self, row_number, col_number): 
        if row_number > self.size or col_number > self.size or row_number < 0 or col_number < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[row_number-1][col_number-1] = 1 
            self.adj[col_number-1][row_number-1] = 1 
        
    def remove_edge(self, row_number, col_number): 
        if row_number > self.size or col_number > self.size or row_number < 0 or col_number < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[row_number-1][col_number-1] = 0 
            self.adj[col_number-1][row_number-1] = 0 
            
    def display(self): 
        for row in self.adj: 
            print()
            for val in row: 
                print('{:4}'.format(val),end="") 

#a sample Graph 
G = Graph(6) 
G.add_edge(1, 5) 
G.add_edge(2, 6)
G.add_edge(3, 6)
G.add_edge(4, 6)
G.add_edge(5, 6)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.remove_edge(1, 4)
G.remove_edge(1, 2)
G.remove_edge(1, 3)

G.display()

"""
Graph --> represnts many real life applications like networks, transportation 
paths of a city, social network connections.
A graph is a set of connected nodes.
Node --> called as vertex and connection between two nodes is called as edge.
For example: connections on a social network, where each vertex represents a 
person and edges represents connections.
"""
"""
A graph can be represented as a square matrix where each element represents 
the edges:
    0 --> no edges
    1 --> an edge
    rows and columns --> vertices
"""
"""
In our example:
    1's --> 3 edges, the 1st vertex is connected to 2nd, 3rd & 4th.
    There are 6 edges in the matrix, if A is coonected to B, then B is 
    connected to A.
Adjacency matrix: it shows if the corresponding vertices are adjacent or not.
"""
"""
adj --> 2D list to store the matrix.
__init__ --> creates the adj matrix and initializes all vaues to 0 with the 
given size(number of vertices).
add_edge() --> adds an edge by setting the corresponding values to 1.
remove_edge() --> sets the values to 0.
"""