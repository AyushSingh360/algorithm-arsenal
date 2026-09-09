from typing import List
from itertools import pairwise


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                nums = []
                # collect all values in this k x k submatrix
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        nums.append(grid[x][y])

                nums.sort()
                # find minimum absolute difference between distinct adjacent values
                best = float("inf")
                for a, b in pairwise(nums):
                    if a != b:
                        best = min(best, abs(a - b))

                ans[i][j] = 0 if best == float("inf") else best

        return ans
