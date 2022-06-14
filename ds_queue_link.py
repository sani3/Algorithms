class LinkQueue:
    """A queue"""
    def __init__(self):
        self.head = None
        self.tail = None

    class Node:
        """A node"""
        def __init__(self, data):
            self.data = data
            self.next = None

    def is_empty(self):
        """Return True if queue is empty otherwise False"""
        return self.tail is None

    def enqueue(self, data):
        """Add an object to the queue"""
        # store away a reference to the node at tail of the queue
        old_tail = self.tail
        # attach a new node with data at the tail
        self.tail = self.Node(data)
        if old_tail is None:
            # if the new node is the first node, head must also hold its reference
            self.head = self.tail
        else:
            # if the new node is not the first node old node's next attribute must reference new node
            old_tail.next = self.tail

    def dequeue(self):
        if self.head.next is not None:
            # if the next attribute of the node at head references another node, retrieve the data attribute
            data = self.head.data
            # set data attribute of head to None
            self.head.data = None
            # head must now reference the node that it, next attribute holds a reference to
            self.head = self.head.next
            return data
        else:
            # if the next attribute of the node at head is None, retrieve the data attribute
            data = self.head.data
            # set data attribute of head to None
            self.head.data = None
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None
            return data


if __name__ == 'main':
    lq = LinkQueue()
    lq.is_empty()
    lq.enqueue(3)
    lq.is_empty()
    lq.dequeue()
    lq.enqueue(3)
    lq.enqueue("Hello all")
    lq.enqueue([2, 3, 4])
    lq.dequeue()
    lq.dequeue()
    lq.enqueue("Hello all")
    lq.dequeue()
    lq.dequeue()
    lq.is_empty()
