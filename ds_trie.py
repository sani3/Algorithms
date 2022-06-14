class Alphabet:
    def __init__(self):
        self.string = list("abcdefghijklmnopqrstuvwxyz")
        self.R = len(self.string)

    def to_index(self, char):
        for index, key in enumerate(self.string):
            if char == key:
                return index

    def to_char(self, place):
        for index, key in enumerate(self.string):
            if place == index:
                return key


class Node:
    def __init__(self):
        self.value = None
        self.link = [None] * 26


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, key, value):
        node = self.root
        alphabet = Alphabet()
        for i in key:
            if not node.link[alphabet.to_index(i)]:
                node.link[alphabet.to_index(i)] = Node()
                node = node.link[alphabet.to_index(i)]
            else:
                node = node.link[alphabet.to_index(i)]
        node.value = value

    def search(self, key):
        node = self.root
        alphabet = Alphabet()
        i = 0
        while i <= len(key)-1:
            if not alphabet.to_index(key[i]):
                return None
            else:
                node = node.link[alphabet.to_index(key[i])]
                if i < len(key)-1:
                    i += 1
                elif i == len(key)-1:
                    return node.value

# collect(), wildcardmatch(), delete(), longestprefix()