from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_size = len(q)
            rightmost_val = None

            for i in range(level_size):
                node = q.popleft()
                rightmost_val = node.val  # last node processed at this level

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(rightmost_val)

        return res
