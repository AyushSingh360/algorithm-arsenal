# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Tuple[Optional[TreeNode], int]:
            # Returns: (subtree root containing all deepest nodes, max depth)
            if node is None:
                return None, 0

            # Recursively get results from left and right subtrees
            left_subtree, left_depth = dfs(node.left)
            right_subtree, right_depth = dfs(node.right)

            # Decision logic:
            # - If left depth > right depth: deepest nodes are only on left side
            # - If right depth > left depth: deepest nodes are only on right side
            # - If depths are equal: current node is the LCA (deepest on both sides)
            if left_depth > right_depth:
                return left_subtree, left_depth + 1
            elif left_depth < right_depth:
                return right_subtree, right_depth + 1
            else:
                return node, left_depth + 1

        return dfs(root)[0]
