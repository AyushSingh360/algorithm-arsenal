# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) splits
        index = {val: i for i, val in enumerate(inorder)}

        def helper(pre_l: int, in_l: int, size: int) -> Optional[TreeNode]:
            if size <= 0:
                return None

            root_val = preorder[pre_l]
            root_in_idx = index[root_val]
            left_size = root_in_idx - in_l

            left = helper(pre_l + 1, in_l, left_size)
            right = helper(pre_l + 1 + left_size, root_in_idx + 1, size - 1 - left_size)

            return TreeNode(root_val, left, right)

        return helper(0, 0, len(preorder))
