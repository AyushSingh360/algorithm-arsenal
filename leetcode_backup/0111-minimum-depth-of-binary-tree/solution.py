from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # if one side is missing, you must go down the other side to reach a leaf
        if root.left is None:
            return 1 + self.minDepth(root.right)

        if root.right is None:
            return 1 + self.minDepth(root.left)

        # both children exist: take the smaller depth
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
