# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res: List[int] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            res.append(node.val)  # root
            dfs(node.left)  # left
            dfs(node.right)  # right

        dfs(root)
        return res
