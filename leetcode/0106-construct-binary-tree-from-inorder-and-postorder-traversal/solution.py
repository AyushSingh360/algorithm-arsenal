# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # value -> index in inorder for O(1) splits
        idx = {val: i for i, val in enumerate(inorder)}
        # start from the last postorder index (root of whole tree)
        self.post_i = len(postorder) - 1

        def helper(l: int, r: int) -> Optional[TreeNode]:
            # build tree from inorder[l:r+1]
            if l > r:
                return None

            root_val = postorder[self.post_i]
            self.post_i -= 1
            root = TreeNode(root_val)

            # inorder index of root
            m = idx[root_val]

            # IMPORTANT: build right subtree first (because postorder is left, right, root)
            root.right = helper(m + 1, r)
            root.left = helper(l, m - 1)

            return root

        return helper(0, len(inorder) - 1)
