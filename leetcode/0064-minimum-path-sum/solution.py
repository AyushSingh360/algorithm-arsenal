class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        # Fill first row (can only come from left)
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # Fill first column (can only come from top)
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # Fill the rest: min(from top, from left) + current cell
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]
