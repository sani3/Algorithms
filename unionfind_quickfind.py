class QuickFind:
    """
    A representation of nodes with paths that represent connection between nodes

    Assumptions:
    1. Reflexive: node p is connected to node p
    2. Symmetric: if node p is connected to node q, node q is connected to node p
    3. Transitive: if node p is connected to node q and node q is connected to node r, node p is connected to node r

    This representation uses a list as the basic data structure
    such that the indexes represents nodes and each unique value is its own connection index
    """

    def __init__(self, number_of_nodes):
        self.nodes = list(range(number_of_nodes))

    def connect(self, node_1, node_2):
        # Add node_1 and node_2 to the same connection_id
        dummy = self.nodes[node_2]
        for node in self.nodes:
            if self.nodes[node] == dummy:
                self.nodes[node] = self.nodes[node_1]

    def connected(self, node_1, node_2):
        return self.nodes[node_1] == self.nodes[node_2]


if __name__ == 'main':

    QF = QuickFind(10)
    QF.connect(0, 5)
    QF.connect(5, 6)
    QF.connect(1, 2)
    QF.connect(2, 7)
    QF.connect(8, 3)
    QF.connect(3, 4)
    QF.connect(4, 9)

    print(QF.connected(2, 3))
    print(QF.connected(7, 1))
