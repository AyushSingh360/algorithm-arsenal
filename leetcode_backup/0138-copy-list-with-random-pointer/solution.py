# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # Map original node -> copied node
        old_to_new = {}

        # First pass: clone nodes and next pointers
        curr = head
        dummy = Node(0)
        tail = dummy

        while curr:
            clone = Node(curr.val)
            old_to_new[curr] = clone
            tail.next = clone
            tail = clone
            curr = curr.next

        # Second pass: set random pointers
        curr = head
        while curr:
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            else:
                old_to_new[curr].random = None
            curr = curr.next

        return dummy.next
