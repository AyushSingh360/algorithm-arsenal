# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while cur or stack:
            # go as left as possible
            while cur:
                stack.append(cur)
                cur = cur.left

            # process the next smallest node
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val

            # go to right subtree
            cur = cur.right
