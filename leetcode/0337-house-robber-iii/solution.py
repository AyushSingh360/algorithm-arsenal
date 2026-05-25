# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Returns (rob_this_node, skip_this_node)
            if not node:
                return 0, 0
            
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            
            # If we rob this node, we must skip its children
            rob_this = node.val + left_skip + right_skip
            
            # If we skip this node, children can be either robbed or skipped
            skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)
            
            return rob_this, skip_this
        
        return max(dfs(root))
