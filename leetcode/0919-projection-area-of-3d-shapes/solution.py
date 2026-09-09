from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # top view (xy): each non-zero cell contributes 1
        xy = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)

        # front view (yz): max in each row
        yz = sum(max(row) for row in grid)

        # side view (zx): max in each column
        zx = 0
        for j in range(n):
            col_max = 0
            for i in range(n):
                col_max = max(col_max, grid[i][j])
            zx += col_max

        return xy + yz + zx
