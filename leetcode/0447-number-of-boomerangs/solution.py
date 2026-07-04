import collections
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for x1, y1 in points:
            count = collections.Counter()
            for x2, y2 in points:
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                ans += 2 * count[d]
                count[d] += 1
        return ans
