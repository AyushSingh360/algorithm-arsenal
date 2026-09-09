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
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root

        # Start with the leftmost node of the current level
        leftmost = root

        # Since it's a perfect binary tree, if leftmost.left is None,
        # we've reached the leaves
        while leftmost.left:
            head = leftmost
            # Traverse the current level using next pointers
            while head:
                # Connect children of the same parent
                head.left.next = head.right

                # Connect right child to next subtree's left child
                if head.next:
                    head.right.next = head.next.left

                head = head.next

            # Move down to the leftmost node of the next level
            leftmost = leftmost.left

        return root
