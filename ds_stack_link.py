class LinkStack:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def push(self, data):
        top = self.head
        self.head = self.Node(data)
        self.head.next = top

    def pop(self):
        data = self.head.data
        self.head.data = None
        self.head = self.head.next
        return data

    def is_empty(self):
        return self.head is None


if __name__ == 'main':
    LStack = LinkStack()
    LStack.is_empty()
    LStack.push(20)
    LStack.push([6, 8, 0])
    LStack.pop()
    LStack.push("God of all")
    LStack.pop()
    LStack.pop()
    LStack.is_empty()
