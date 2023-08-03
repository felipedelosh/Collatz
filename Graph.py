"""
FelipedelosH
2023

"""
class Graph:
    """
    set edges and nodes 

    node is a id, edge is a interconector (destination, weight)
    the pivot is to move
    """
    def __init__(self) -> None:
        self.pivot = None
        self.nodes = []
        self.edges = {}


    def setPivot(self, pivot):
        """
        Se a pivot to mouve.
        """
        if pivot in self.nodes:
            self.pivot = pivot


    def addNode(self, x):
        """
        Add node key
        """
        if x not in self.nodes:
            self.nodes.append(x)


    def addEdge(self, origin ,destination, weight):
        """
        Conect two nodes origin->destination with cost
        """
        try:
            if not origin in self.edges.keys():
                self.edges[origin] = []
            # Add
            self.edges[origin].append((destination, weight))
        except:
            pass

        
    def step(self, destination):
        """
        Enter a destination and mouve if is hable
        """
        if self.pivot != None:
            for i in self.edges[self.pivot]:
                if i[0] == destination:
                    self.pivot = i[0]
                    break
