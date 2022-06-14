# Binary heap implementation with "Complete Binary Tree" represented as a list
# List index represents node
# A parent node a[i] has two children at a[2*i+1] and a[2*i+2] on the left and right respectively
# A child at node a[i] has it parent node at a[(i-1)//2]
# Any parent node must have a key that is greater than the keys at children nodes (heap order)
# This code also implements a priority queue with the binary heap

class BinaryHeap:
    def __init__(self):
        self.queue = []

    def swap(self, node1, node2):
        """(int, int) >- None

        exchange the keys at node1 and node2
        """
        dummy = self.queue[node1]
        self.queue[node1] = self.queue[node2]
        self.queue[node2] = dummy
        # O(1)

    def swim(self, node):
        """(int) >- None

        move key at node up the heap to ensure heap order
        """
        while self.queue[node] > self.queue[(node - 1) // 2]:
            self.swap(node, (node - 1) // 2)
            node = (node - 1) // 2
            if node == 0:
                break
            # O(~log N)

    def sink(self, node):
        """(int) >- None

        move key at node down the heap to ensure heap order
        """
        while node <= len(self.queue) - 1:
            # if both children exists, get index of the child with maximum value
            if 2 * node + 1 < len(self.queue) - 1 and 2 * node + 2 <= len(self.queue) - 1:
                if self.queue[2 * node + 1] > self.queue[2 * node + 2]:
                    max_child_index = 2 * node + 1
                else:
                    max_child_index = 2 * node + 2
            # if only left child exists, get index of left child
            elif 2 * node + 1 == len(self.queue) - 1:
                max_child_index = 2 * node + 1
            # if no children exists, stop
            else:
                break
            if self.queue[node] < self.queue[max_child_index]:
                # swap node with max_child_index
                self.swap(node, max_child_index)
                node = max_child_index
            else:
                break
            # O(~log N)

    def insert(self, key):
        """(any) >- None

        insert a new key
        """
        self.queue.append(key)
        self.swim(len(self.queue) - 1)
        # O(log N)

    def remove(self, node):
        """(int) >- None

        remove the key at a node
        """
        assert node in range(len(self.queue)), "node does not exist"
        self.swap(node, -1)
        self.queue.pop()
        self.sink(node)
        # O(log N)

    def heapsort(self):
        """(None) >- None

        return sorted keys
        """
        result = []
        while not len(self.queue) == 0:
            self.swap(0, -1)
            result.append(self.queue.pop())
            self.sink(0)
        return result
    # O(Nlog N)


if __name__ != 'main':
    # Priority Queue
    p = BinaryHeap()
    p.insert(3)
    p.insert(4)
    p.insert(6)
    p.insert(2)
    p.insert(8)
    p.insert(12)
    p.insert(10)
    p.insert(15)
    p.insert(13)
    p.insert(0)

    p.remove(1)
    p.remove(2)
    p.remove(0)
    p.heapsort()

    pq = BinaryHeap()
    pq.insert("z")
    pq.insert("q")
    pq.insert("v")
    pq.insert("k")
    pq.insert("a")
    pq.insert("i")
    pq.insert("m")
    pq.insert("o")
    pq.insert("c")

    pq.heapsort()
