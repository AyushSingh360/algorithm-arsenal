from typing import List
from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # For each value, keep a list of its last (up to) 3 indices
        pos = defaultdict(list)
        ans = float("inf")

        for i, x in enumerate(nums):
            pos[x].append(i)
            # We only need the last 3 positions for this value
            if len(pos[x]) > 3:
                pos[x].pop(0)

            # If we have at least 3 occurrences, compute distance
            if len(pos[x]) == 3:
                i1, i2, i3 = pos[x]
                # For any i < j < k, this formula simplifies to 2 * (k - i)
                dist = 2 * (i3 - i1)
                ans = min(ans, dist)

        return -1 if ans == float("inf") else ans
