# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = None

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return

            inorder(node.left)

            # detect violation
            if self.prev and self.prev.val > node.val:
                # first violation
                if not self.first:
                    self.first = self.prev
                    self.second = node
                else:
                    # second violation
                    self.second = node
            self.prev = node

            inorder(node.right)

        inorder(root)
        # swap the two wrong nodes
        self.first.val, self.second.val = self.second.val, self.first.val
