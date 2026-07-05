# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # 1. Traverse the tree to find the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 2. Node with 0 or 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # 3. Node with 2 children:
            #    find inorder successor (minimum in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left

            # Copy successor's value to current node
            root.val = successor.val
            # Delete the successor node from right subtree
            root.right = self.deleteNode(root.right, successor.val)

        return root
