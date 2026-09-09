from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.freq = 1
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_first(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: Node) -> Node:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        return node

    def remove_last(self) -> Node:
        if self.head.next is self.tail:
            return None  # should not happen if used correctly
        return self.remove(self.tail.prev)

    def is_empty(self) -> bool:
        return self.head.next is self.tail


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.node_map: dict[int, Node] = {}  # key -> Node
        self.freq_map: defaultdict[int, DoublyLinkedList] = defaultdict(
            DoublyLinkedList
        )  # freq -> list

    def get(self, key: int) -> int:
        if self.capacity == 0 or key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._increase_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._increase_freq(node)
            return

        if self.size == self.capacity:
            # evict LFU (least freq, then LRU within that freq)
            l = self.freq_map[self.min_freq]
            evicted = l.remove_last()
            del self.node_map[evicted.key]
            self.size -= 1

        # insert new node
        node = Node(key, value)
        self.node_map[key] = node
        self.freq_map[1].add_first(node)
        self.min_freq = 1
        self.size += 1

    def _increase_freq(self, node: Node) -> None:
        freq = node.freq
        l = self.freq_map[freq]
        l.remove(node)
        if l.is_empty():
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        node.freq += 1
        self.freq_map[node.freq].add_first(node)
