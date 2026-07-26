# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Edge case: empty tree
        if not root:
            return []

        # State variables for inorder traversal
        self.prev = None  # previous node value
        self.cnt = 0  # current value frequency
        self.mx = 0  # maximum frequency found so far
        self.ans: List[int] = []  # list of modes

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return

            # Traverse left subtree
            inorder(node.left)

            # Process current node
            if self.prev is None or self.prev != node.val:
                # New value, reset count
                self.cnt = 1
            else:
                # Same value as previous, increment count
                self.cnt += 1

            # Update modes based on current count
            if self.cnt > self.mx:
                self.mx = self.cnt
                self.ans = [node.val]
            elif self.cnt == self.mx:
                self.ans.append(node.val)

            # Update prev to current value
            self.prev = node.val

            # Traverse right subtree
            inorder(node.right)

        inorder(root)
        return self.ans
