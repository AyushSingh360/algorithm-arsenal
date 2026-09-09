from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Total sum of all cells
        total = sum(sum(row) for row in grid)
        if total % 2 == 1:
            return False
        half = total // 2

        # Check horizontal cuts: prefix over rows
        pref = 0
        for i in range(m):
            pref += sum(grid[i])
            # cut is after row i, so i must not be last row
            if i != m - 1 and pref == half:
                return True

        # Check vertical cuts: prefix over columns
        pref = 0
        for j in range(n):
            col_sum = 0
            for i in range(m):
                col_sum += grid[i][j]
            pref += col_sum
            # cut is after column j, so j must not be last column
            if j != n - 1 and pref == half:
                return True

        return False
