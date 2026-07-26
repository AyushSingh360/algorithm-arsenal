from collections import Counter
from typing import List, Optional


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = Counter()

        def dfs(node):
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            freq[total] += 1
            return total

        dfs(root)
        max_freq = max(freq.values())
        return [s for s, c in freq.items() if c == max_freq]
