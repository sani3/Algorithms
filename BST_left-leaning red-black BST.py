class Node:
    def __init__(self, key, value, red=True):
        self.key = key
        self.value = value
        self.red = red
        self.left = None
        self.right = None
        self.children = 0


class RedBlack:
    def __init__(self):
        self.root = None

    def insert(self, key, value, red):
        if self.root is None:
            self.root = Node(key, value, False)
        else:
            node = self.root
            if key < node.key:
                #
            elif key > node.key and node.right is None:
                node.right = Node(key, value)
                node = rotate_left(node)
            elif key < node.key and node.left is not None:
                node.left = self.insert(key, value)



def rotate_left(node):
    pointer = node.right
    node.right = pointer.left
    pointer.left = node
    pointer.red = node.red
    node.red = True
    node = pointer
    return node


def rotate_right(node):
    pointer = node.left
    node.left = pointer.right
    pointer.right = node
    pointer.red = node.red
    node.red = True
    node = pointer
    return node


def flip(node):
    node.red = True
    node.left.red = False
    node.right.red = False


def is_red(node):
    return node.red
