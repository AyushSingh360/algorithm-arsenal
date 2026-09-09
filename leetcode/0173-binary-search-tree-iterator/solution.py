# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # Stack will store the path to the next smallest element
        self.stack = []
        self._push_left_branch(root)

    # Push all left children starting from node onto the stack
    def _push_left_branch(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Top of stack is the next smallest node
        node = self.stack.pop()
        val = node.val
        # If there is a right subtree, its leftmost node is the next candidate
        if node.right:
            self._push_left_branch(node.right)
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
