# a set of two elements represents a undirected edges
# a tuple of two elements represents a directed edge
# representations include: adjacency matrix, array of adjacency list, and array of edges

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def add_edge(self, node1, node2):
        self.edges.add((node1, node2))
        self.nodes.add(node1)
        self.nodes.add(node2)

    def count_edges(self):
        return len(self.edges)

    def count_nodes(self):
        return len(self.nodes)


if __name__ != 'main':
    net = Graph()
    net.add_edge(3, 2)
    net.add_edge(1, 4)
    net.add_edge(6, 4)
    net.add_edge(2, 1)
    net.nodes
    net.edges
