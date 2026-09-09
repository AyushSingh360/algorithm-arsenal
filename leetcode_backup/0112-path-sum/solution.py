from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # If it's a leaf, check if the path sum matches
        if not root.left and not root.right:
            return targetSum == root.val

        # Recurse on children with reduced target
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(
            root.right, remaining
        )
