class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        sums = set()

        # For each cell as the top corner of a rhombus
        for i in range(m):
            for j in range(n):
                # Size 0 rhombus (just the single cell)
                sums.add(grid[i][j])

                # Try all possible rhombus sizes
                # k = 1 means the rhombus extends 1 cell in each diagonal direction
                k = 1
                while i + 2 * k < m and j - k >= 0 and j + k < n:
                    # Calculate the rhombus border sum with top corner at (i, j) and size k
                    total = 0

                    # Top to right: (i, j) -> (i+k, j+k)
                    for step in range(k):
                        total += grid[i + step][j + step]

                    # Right to bottom: (i+k, j+k) -> (i+2k, j)
                    for step in range(k):
                        total += grid[i + k + step][j + k - step]

                    # Bottom to left: (i+2k, j) -> (i+k, j-k)
                    for step in range(k):
                        total += grid[i + 2 * k - step][j - step]

                    # Left to top: (i+k, j-k) -> (i, j)
                    for step in range(k):
                        total += grid[i + k - step][j - k + step]

                    sums.add(total)
                    k += 1

        # Get the 3 largest distinct sums
        result = sorted(sums, reverse=True)[:3]
        return result
