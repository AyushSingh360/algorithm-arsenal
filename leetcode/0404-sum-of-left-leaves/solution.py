# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = 0

        # check left child
        if root.left:
            # if left child is a leaf
            if not root.left.left and not root.left.right:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)

        # always explore right subtree
        total += self.sumOfLeftLeaves(root.right)

        return total
