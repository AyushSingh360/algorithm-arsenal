from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # pref[i][j] = sum of rectangle (0,0) to (i-1, j-1)
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += grid[i][j]
                pref[i + 1][j + 1] = pref[i][j + 1] + row_sum

        ans = 0
        # For each row, find how many prefix sums <= k from the left
        for i in range(1, m + 1):
            j = 1
            while j <= n and pref[i][j] <= k:
                j += 1
            ans += j - 1

        return ans
