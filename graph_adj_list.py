# a set of two elements represents a undirected edges
# a tuple of two elements represents a directed edge
# representations include: adjacency matrix, array of adjacency list, and array of edges

class Graph:
    def __init__(self):
        self.nodes = [None]*10

    def add_edge(self, node1, node2):
        if self.nodes[node1] is None:
            self.nodes[node1] = set([node2])
        else:
            self.nodes[node1].add(node2)
        if self.nodes[node2] is None:
            self.nodes[node2] = set([node1])
        else:
            self.nodes[node2].add(node1)

    def count_edges(self):
        return len(self.edges)

    def count_nodes(self):
        return len(self.nodes)


if __name__ != 'main':
    net = Graph()
    net.add_edge(3, 2)
    net.add_edge(1, 4)
    net.add_edge(6, 4)
    net.add_edge(6, 3)
