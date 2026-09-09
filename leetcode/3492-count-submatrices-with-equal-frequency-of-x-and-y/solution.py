from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # prefix sums over rows for each column
        sumX = [0] * cols
        sumY = [0] * cols
        res = 0

        for i in range(rows):
            rx = 0  # X count in current row prefix [0..j]
            ry = 0  # Y count in current row prefix [0..j]
            for j in range(cols):
                if grid[i][j] == "X":
                    rx += 1
                elif grid[i][j] == "Y":
                    ry += 1

                # prefix rectangle (0,0) to (i,j) total X/Y using compressed prefix sums
                sumX[j] += rx
                sumY[j] += ry

                # valid if equal X and Y and at least one X
                if sumX[j] > 0 and sumX[j] == sumY[j]:
                    res += 1

        return res
