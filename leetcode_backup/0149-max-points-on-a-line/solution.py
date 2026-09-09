from typing import List
from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        ans = 1
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            max_on_line = 0

            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                # normalize sign so each line has a unique slope key
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slope = (dy, dx)
                slopes[slope] += 1
                max_on_line = max(max_on_line, slopes[slope])

            ans = max(ans, max_on_line + 1)

        return ans
