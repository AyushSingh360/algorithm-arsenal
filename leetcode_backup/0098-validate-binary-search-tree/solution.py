# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low, high):
            if not node:
                return True

            # Current node must be strictly between low and high
            if not (low < node.val < high):
                return False

            # Left subtree: high bound becomes node.val
            # Right subtree: low bound becomes node.val
            return helper(node.left, low, node.val) and helper(
                node.right, node.val, high
            )

        return helper(root, float("-inf"), float("inf"))
