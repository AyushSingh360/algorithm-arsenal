from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # problem guarantees at least 1 node, but keep safe

        q = deque([root])
        level = 1
        max_level = 1
        max_sum = float("-inf")

        while q:
            level_size = len(q)
            level_sum = 0

            for _ in range(level_size):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            level += 1

        return max_level
