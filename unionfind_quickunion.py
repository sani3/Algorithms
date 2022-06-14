class QuickUnion:
    """
    A representation of nodes with paths that represent connection between nodes

    Assumptions:
    1. Reflexive: node p is connected to node p
    2. Symmetric: if node p is connected to node q, node q is connected to node p
    3. Transitive: if node p is connected to node q and node q is connected to node r, node p is connected to node r

    This representation uses a list as the basic data structure such that
        Ihe indexes represents "nodes",
        The value at an index represents the "parent node" of the noe at the index
        If the value at an index is the same as the index, then the node at the same index is a "root"
            Connected nodes have the same root
    """

    def __init__(self, number_of_nodes):
        self.nodes = list(range(number_of_nodes))

    def root(self, node):
        while node != self.nodes[node]:
            # self.nodes[node] = self.nodes[self.nodes[node]] ## An improvements called "Path compression"
            node = self.nodes[node]
        return node

    # an improvement on connect maintains a list that keeps a weight (number) of children of each root node
    # such that only a root of lower weight can be joined to a root of higher weight
    def connect(self, node_1, node_2):
        # Add node_1 and node_2 to the same root
        node_1_root = self.root(node_1)
        node_2_root = self.root(node_2)
        self.nodes[node_1_root] = self.nodes[node_2_root]

    def connected(self, node_1, node_2):
        node_1_root = self.root(node_1)
        node_2_root = self.root(node_2)
        return self.nodes[node_1_root] == self.nodes[node_2_root]


if __name__ != 'main':
    QU = QuickUnion(10)
    QU.connect(4, 3)
    QU.connect(3, 8)
    QU.connect(6, 5)
    QU.connect(9, 4)
    QU.connect(2, 1)
    print(QU.connected(8, 9))
    print(QU.connected(5, 4))
    QU.connect(5, 0)
    QU.connect(7, 2)
    QU.connect(6, 1)
    QU.connect(7, 3)

