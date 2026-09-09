from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node: Optional[TreeNode], cur_sum: int, path: List[int]) -> None:
            if not node:
                return

            cur_sum += node.val
            path.append(node.val)

            # If leaf and sum matches, store a copy
            if not node.left and not node.right and cur_sum == targetSum:
                res.append(path[:])

            dfs(node.left, cur_sum, path)
            dfs(node.right, cur_sum, path)

            # backtrack
            path.pop()

        dfs(root, 0, [])
        return res
