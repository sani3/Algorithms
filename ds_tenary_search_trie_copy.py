from ds_queue_list import ListQueue


class Node:
    def __init__(self):
        self.label = None
        self.links = [None]*3  # left -> links[0], center -> node.links[1], right -> node.links[2]
        self.value = None


class TenarySearchTrie:
    def __init__(self):
        self.root = Node()

    def insert(self, key, value):
        """(str, any) -> None

        insert key-value pair to trie
        """
        node = self.root
        i = 0
        while i <= len(key) - 1:
            if node.label is None:
                node.label = key[i]
                if i == len(key) - 1:
                    node.value = value
                    return
                if node.links[1] is None:
                    node.links[1] = Node()
                node = node.links[1]
                i += 1
            else:
                if key[i] < node.label:
                    if node.links[0] is None:
                        node.links[0] = Node()
                    node = node.links[0]
                elif key[i] > node.label:
                    if node.links[2] is None:
                        node.links[2] = Node()
                    node = node.links[2]
                elif key[i] == node.label:
                    if i == len(key) - 1:
                        node.value = value
                        return
                    if node.links[1] is None:
                        node.links[1] = Node()
                    node = node.links[1]
                    i += 1

    def search(self, key):
        """(str) -> any

        return the value associated with key in trie
        """
        node = self.root
        i = 0
        while i <= len(key)-1:
            if node is None or node.label is None:
                return None
            else:
                if key[i] == node.label:
                    if i == len(key) - 1:
                        return node.value
                    node = node.links[1]
                    i += 1
                elif key[i] < node.label:
                    node = node.links[0]
                elif key[i] > node.label:
                    node = node.links[2]

    def gather(self):
        node = self.root
        q = ListQueue()
        self.get_key(node, q)

    def get_key(self, node, q):
        if node is not None:
            q.enqueue(node.label)
            if node.value is not None:
                print(q.queue, node.value)
            node = node.links[1]
            self.get_key(node, q)
        else:
            return





t = TenarySearchTrie()
t.insert("shells", 15)
t.insert("surely", 1)
t.insert("sells", 11)
t.insert("sea", 14)
t.insert("by", 4)
t.insert("are", 12)
t.insert("the", 8)
t.insert("she", 0)

