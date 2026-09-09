# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        MOD = 10**9 + 7
        self.max_product = 0

        # First pass: Calculate total sum of tree
        def get_sum(node):
            if not node:
                return 0
            return node.val + get_sum(node.left) + get_sum(node.right)

        total_sum = get_sum(root)

        # Second pass: For each subtree, calculate product
        def dfs(node):
            if not node:
                return 0

            # Calculate subtree sum
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            subtree_sum = node.val + left_sum + right_sum

            # Calculate product if we cut above this subtree
            product = subtree_sum * (total_sum - subtree_sum)
            self.max_product = max(self.max_product, product)

            return subtree_sum

        dfs(root)
        return self.max_product % MOD
