# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Base case: if root is None or matches p or q, return it
        if not root or root == p or root == q:
            return root

        # Recurse on left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides are non-null, p and q are in different subtrees → root is LCA
        if left and right:
            return root

        # Otherwise, LCA is in the non-null side (or None if neither side has p/q)
        return left if left else right
