from bisect import bisect_left
from typing import List


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        if k <= 1:
            return 0

        # For k = 2, just maximize Manhattan distance directly.
        if k == 2:
            vals1 = [x + y for x, y in points]
            vals2 = [x - y for x, y in points]
            return max(max(vals1) - min(vals1), max(vals2) - min(vals2))

        n = len(points)
        perimeter = 4 * side

        def pos(x: int, y: int) -> int:
            if y == 0:  # bottom: (0,0) -> (side,0)
                return x
            if x == side:  # right: (side,0) -> (side,side)
                return side + y
            if y == side:  # top: (side,side) -> (0,side)
                return 3 * side - x
            return 4 * side - y  # left: (0,side) -> (0,0)

        arr = sorted(pos(x, y) for x, y in points)
        arr2 = arr + [p + perimeter for p in arr]

        def can(d: int) -> bool:
            # For k >= 3, answer never exceeds side.
            # On the square boundary, for d <= side, Manhattan >= d
            # is equivalent to circular boundary separation >= d.
            m = 2 * n

            nxt = [m] * m
            j = 0
            for i in range(m):
                if j < i:
                    j = i
                while j < m and arr2[j] < arr2[i] + d:
                    j += 1
                nxt[i] = j

            LOG = (k - 1).bit_length()
            up = [nxt]
            for _ in range(1, LOG):
                prev = up[-1]
                up.append([prev[prev[i]] if prev[i] < m else m for i in range(m)])

            for start in range(n):
                cur = start
                steps = k - 1
                bit = 0

                while steps and cur < m:
                    if steps & 1:
                        cur = up[bit][cur]
                    steps >>= 1
                    bit += 1

                if cur < start + n and arr2[cur] - arr2[start] <= perimeter - d:
                    return True

            return False

        lo, hi = 0, side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
