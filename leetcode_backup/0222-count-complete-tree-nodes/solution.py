from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def left_height(node: Optional[TreeNode]) -> int:
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def right_height(node: Optional[TreeNode]) -> int:
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        lh = left_height(root)
        rh = right_height(root)

        # Perfect tree: use formula 2^h - 1
        if lh == rh:
            return (1 << lh) - 1

        # Otherwise, count recursively
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
