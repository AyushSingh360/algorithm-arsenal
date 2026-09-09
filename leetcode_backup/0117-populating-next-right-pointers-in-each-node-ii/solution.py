# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        # `curr` iterates the current level using already-established next pointers
        curr = root

        while curr:
            dummy = Node(0)  # dummy head for the next level
            tail = dummy  # tail builds the linked list (via next) of next level
            # Traverse current level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            # Move to the first node in the next level
            curr = dummy.next

        return root
