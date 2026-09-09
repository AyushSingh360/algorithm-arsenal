from typing import List
from collections import defaultdict

MOD = 10**9 + 7


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        by_y = defaultdict(int)
        for x, y in points:
            by_y[y] += 1

        # count of horizontal segments on each y
        segs = []
        for y, c in by_y.items():
            if c >= 2:
                segs.append(c * (c - 1) // 2)

        if len(segs) < 2:
            return 0

        ans = 0
        pref = 0
        for s in segs:
            ans = (ans + s * pref) % MOD
            pref += s

        return ans
