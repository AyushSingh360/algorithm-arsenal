# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict

        # prefix_count[p] = number of times prefix sum p has occurred on the path from root to current node
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # base: a path that exactly equals targetSum from the root

        self.ans = 0

        def dfs(node, cur_sum):
            if not node:
                return
            cur_sum += node.val
            # number of valid paths ending at current node is count of (cur_sum - targetSum) seen earlier
            self.ans += prefix_count[cur_sum - targetSum]

            # include current prefix sum before traversing children
            prefix_count[cur_sum] += 1
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
            # backtrack: remove current prefix before returning up the recursion stack
            prefix_count[cur_sum] -= 1

        dfs(root, 0)
        return self.ans
