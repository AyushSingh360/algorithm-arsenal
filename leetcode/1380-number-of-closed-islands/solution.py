class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 1:
                return
            grid[r][c] = 1  # mark visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Remove every land component touching the boundary.
        for r in range(m):
            for c in (0, n - 1):
                if grid[r][c] == 0:
                    dfs(r, c)

        for c in range(n):
            for r in (0, m - 1):
                if grid[r][c] == 0:
                    dfs(r, c)

        # Remaining land components are closed islands.
        count = 0
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r, c)

        return count
