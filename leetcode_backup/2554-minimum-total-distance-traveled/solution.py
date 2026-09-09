from functools import lru_cache
from math import inf


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort robots and factories by position
        robot.sort()
        factory.sort()  # sort by position automatically [pos, limit][web:4][web:5]

        n, m = len(robot), len(factory)

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            """
            Minimum total distance to repair robots[i:] using factories[j:][web:4][web:5]
            """
            # All robots assigned
            if i == n:
                return 0
            # No factories left but robots remain -> impossible large cost
            if j == m:
                return inf

            # Option 1: skip this factory
            best = dp(i, j + 1)

            # Option 2: assign k robots starting from i to factory j
            pos, cap = factory[j]
            dist_sum = 0
            for k in range(cap):
                if i + k >= n:
                    break
                dist_sum += abs(robot[i + k] - pos)
                best = min(best, dist_sum + dp(i + k + 1, j + 1))

            return best

        return dp(0, 0)
