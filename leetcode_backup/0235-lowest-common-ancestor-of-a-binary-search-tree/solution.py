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
        # Make sure p_val <= q_val to simplify comparisons (optional)
        p_val, q_val = sorted([p.val, q.val])

        curr = root
        while curr:
            if curr.val < p_val:
                # Both nodes are in the right subtree
                curr = curr.right
            elif curr.val > q_val:
                # Both nodes are in the left subtree
                curr = curr.left
            else:
                # Split point: p and q are on different sides,
                # or curr equals one of p or q → this is the LCA
                return curr

        return None  # Should not be reached given the problem constraints
