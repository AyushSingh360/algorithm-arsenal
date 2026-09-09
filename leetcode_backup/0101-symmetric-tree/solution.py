# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # both null → symmetric
            if not left and not right:
                return True
            # one null or value mismatch → not symmetric
            if not left or not right or left.val != right.val:
                return False
            # mirror check: left.left vs right.right, left.right vs right.left
            return is_mirror(left.left, right.right) and is_mirror(
                left.right, right.left
            )

        return is_mirror(root.left, root.right)
