# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        previous = None
        minimum = float("inf")

        def inorder(node):
            nonlocal previous, minimum

            if node is None:
                return

            inorder(node.left)

            if previous is not None:
                minimum = min(minimum, node.val - previous)

            previous = node.val

            inorder(node.right)

        inorder(root)
        return minimum
