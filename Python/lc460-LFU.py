import collections


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        n = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = n
        n.prev = node

    def delete(self, node=None):
        if not node:
            node = self.tail.prev
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.key_node = {}
        self.freq_dbl = {}
        self.min_freq = 0

    def _update(self, node):
        freq = node.freq
        self.freq_dbl[freq].delete(node)
        if freq == self.min_freq and not self.freq_dbl[freq]:
            self.min_freq += 1

        node.freq += 1
        self.freq_dbl[freq + 1].insert(node)

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            self._update(node)
            node.val = value
        else:
            if self.capacity == self.size:
                node = self.freq_dbl[self.min_freq].delete()
                del self.key_node[node.key]
                self.size -= 1
            node = Node(key, value)
            self.key_node[key] = node
            self.freq_dbl[1].insert(node)
            self.min_freq = 1
            self.size += 1

cache = LFUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.get(3)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)