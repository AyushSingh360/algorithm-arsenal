class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.map = {}  # key -> Node

        # dummy head and tail to avoid edge-case checks
        self.head = Node(0, 0)  # most recently used is next to head
        self.tail = Node(0, 0)  # least recently used is prev to tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # helper: remove node from linked list
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # helper: insert node right after head (mark as most recently used)
    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1

        node = self.map[key]
        # move this node to front (most recently used)
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            # update value and move to front
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.map) == self.cap:
                # evict least recently used: node before tail
                lru = self.tail.prev
                self._remove(lru)
                del self.map[lru.key]

            new_node = Node(key, value)
            self.map[key] = new_node
            self._add_to_front(new_node)
