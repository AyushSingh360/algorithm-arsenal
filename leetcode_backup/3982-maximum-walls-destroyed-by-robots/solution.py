from bisect import bisect_left
from typing import List


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)

        # Pair robots with distances and sort by position
        rd = sorted(zip(robots, distance))  # (pos, dist) [web:5]
        robots_sorted = [x for x, _ in rd]
        dist_sorted = [d for _, d in rd]

        # Sort walls [web:5]
        walls.sort()

        # dp[i][dir]: max walls destroyed using robots[0..i],
        # where dir = 0 means robot i is considered with "next robot goes left",
        # dir = 1 means "next robot goes right". [web:5]
        dp = [[-1, -1] for _ in range(n)]

        def count_walls(l: int, r: int) -> int:
            # number of walls in [l, r] inclusive using prefix via bisect [web:5]
            if l > r:
                return 0
            left_idx = bisect_left(walls, l)
            right_idx = bisect_left(walls, r + 1)
            return right_idx - left_idx

        def dfs(i: int, direction: int) -> int:
            if i < 0:
                return 0
            if dp[i][direction] != -1:
                return dp[i][direction]

            pos = robots_sorted[i]
            rng = dist_sorted[i]

            # Option 1: fire left [web:5]
            leftL = pos - rng
            # bullet cannot pass previous robot at robots_sorted[i-1] [web:5]
            if i > 0:
                leftL = max(leftL, robots_sorted[i - 1] + 1)
            leftR = pos
            gain_left = count_walls(leftL, leftR) + dfs(i - 1, 0)

            # Option 2: fire right [web:5]
            rightL = pos
            rightR = pos + rng
            if i + 1 < n:
                # next robot index is i+1; how far we can go depends on its shot direction [web:5]
                next_pos = robots_sorted[i + 1]
                next_rng = dist_sorted[i + 1]
                if direction == 0:
                    # next robot will shoot left, so its left bullet can reach next_pos - next_rng [web:5]
                    # our right bullet cannot cross that meeting point
                    rightR = min(rightR, next_pos - next_rng - 1)
                else:
                    # next robot will shoot right, so our bullet cannot reach its position [web:5]
                    rightR = min(rightR, next_pos - 1)

            gain_right = 0
            if rightL <= rightR:
                gain_right = count_walls(rightL, rightR) + dfs(i - 1, 1)

            res = max(gain_left, gain_right)
            dp[i][direction] = res
            return res

        # Start from last robot, assuming that after it, direction is "right" as in editorial [web:5]
        return dfs(n - 1, 1)
