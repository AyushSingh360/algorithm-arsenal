from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n

        # Normalize k in case it's >= total cells
        k %= total

        # Result grid
        ans = [[0] * n for _ in range(m)]

        # For each cell, compute its new position after k shifts
        for i in range(m):
            for j in range(n):
                flat_idx = i * n + j  # 2D -> 1D index [web:5][web:8][web:9]
                new_flat_idx = (flat_idx + k) % total
                new_i, new_j = divmod(
                    new_flat_idx, n
                )  # 1D -> 2D indices [web:5][web:6][web:8][web:9]
                ans[new_i][new_j] = grid[i][j]

        return ans
