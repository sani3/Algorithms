# Implementation of symbol table (key-value pairs) with binary search tree
# Binary Search Tree (BST) is a binary tree in symmetric order
#     each node has a key, value, left and right
#     each node is a root node with at most two subtrees (left and right)
#     all keys of left subtrees are less than root node key
#     all keys of right subtrees are greater than root node key
#     O(logN)
# Other implementation include unordered linked list of key-value pairs O(N)
# Other implementation include ordered arrays of keys and values pairs O(logN):binary search, O(N):insert
from ds_queue_list import ListQueue


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.counter = 0

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def insert(self, key, value):
        if self.root is None:
            self.root = self.Node(key, value)
            self.counter += 1
        else:
            test_root = self.root
            while test_root is not None:
                if key == test_root.key:
                    test_root.value = value
                    return
                elif key < test_root.key:
                    if test_root.left is not None:
                        test_root = test_root.left
                    else:
                        test_root.left = self.Node(key, value)
                        self.counter += 1
                        return
                else:
                    if test_root.right is not None:
                        test_root = test_root.right
                    else:
                        test_root.right = self.Node(key, value)
                        self.counter += 1
                        return

    def search(self, key):
        test_root = self.root
        while test_root is not None:
            if key == test_root.key:
                return test_root.value
            elif key < test_root.key:
                test_root = test_root.left
            else:
                test_root = test_root.right
        return None

    def minimum(self):
        test_root = self.root
        while test_root.left is not None:
            test_root = test_root.left
        return test_root.key

    def maximum(self):
        test_root = self.root
        while test_root.right is not None:
            test_root = test_root.right
        return test_root.key

    # Recursive: traverse() calls a recursive inorder() function
    def traverse(self):
        q = ListQueue()
        self.inorder(self.root, q)
        return q.queue

    def inorder(self, root, q):
        if root is None:
            return
        self.inorder(root.left, q)
        q.enqueue(root.key)
        self.inorder(root.right, q)

    # def delete

# possible ordered operations:
# floor(), ceiling(), select(), order(), size(), rank(),
# All operations can perform in average time complexity proportional to height of the tree
# except traverse which is always in order of N
# But the worst case of time complexity is always O(N) ie if tree is degenerate


if __name__ != 'main':
    b = BinarySearchTree()
    b.insert("k", 11)
    b.insert("l", 12)
    b.insert("j", 10)
    b.search("k")
    b.search("j")
    b.search("l")

    b = BinarySearchTree()
    b.insert(2, 1)
    b.insert(8, 2)
    b.insert(12, 3)
    b.insert(6, 4)
    b.insert(4, 5)
    b.insert(0, 6)
    b.insert(15, 7)
    b.insert(-11, 8)
