from typing import List
from collections import defaultdict


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = 2 * n

        # min distance at each position in [0, 2n)
        dist = [m] * m

        # left -> right: closest same value on the left
        last = {}
        for i in range(m):
            v = nums[i % n]
            if v in last:
                dist[i] = min(dist[i], i - last[v])
            last[v] = i

        # right -> left: closest same value on the right
        nxt = {}
        for i in range(m - 1, -1, -1):
            v = nums[i % n]
            if v in nxt:
                dist[i] = min(dist[i], nxt[v] - i)
            nxt[v] = i

        # compress back to first n indices, merging with their wrapped copy
        best = [0] * n
        for i in range(n):
            best[i] = min(dist[i], dist[i + n])
            if best[i] >= n:
                best[i] = -1

        return [best[q] for q in queries]
