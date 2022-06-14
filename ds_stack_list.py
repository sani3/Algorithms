class ListStack:
    """Stack data structure"""

    def __init__(self, size):
        self.stack = [None] * size
        self.head = -1

    def push(self, data):
        """Push data to the head of the stack"""
        if self.head < len(self.stack) - 1:
            self.head += 1
            self.stack[self.head] = data
        else:
            print("Stack is full")

    def pop(self):
        """Return and remove data at the head of the stack"""
        if self.head >= 0:
            data = self.stack[self.head]
            self.stack[self.head] = None
            self.head -= 1
            return data
        else:
            print("stack is empty")

    def is_empty(self):
        """Return True if stack is empty otherwise return False"""
        return self.head == -1


class SimpleListStack:
    """Stack data structure: This implementation relies on list methods for push and pop"""

    def __init__(self):
        self.stack = []

    def push(self, data):
        """Push data to the head of the stack"""
        self.stack.append(data)

    def pop(self):
        """Return and remove data at the head of the stack"""
        self.stack.pop(-1)

    def is_empty(self):
        """Return True if stack is empty otherwise return False"""
        return self.stack == []


if __name__ == 'main':
    MyStack = ListStack(10)     # MyStack = SimpleListStack()
    MyStack.push(1)
    MyStack.push(2)
    MyStack.pop()
    MyStack.push(4)
    MyStack.push(5)
    MyStack.push(6)
    MyStack.pop()
    MyStack.pop()
    MyStack.pop()
    MyStack.is_empty()


