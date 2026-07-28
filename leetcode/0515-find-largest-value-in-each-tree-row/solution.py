from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        q = deque([root])

        while q:
            level_max = float("-inf")
            for _ in range(len(q)):
                node = q.popleft()
                level_max = max(level_max, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level_max)

        return ans
