from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        # 4-directional moves
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x: int, y: int, px: int, py: int, ch: str) -> bool:
            visited[x][y] = True

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                # bounds
                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                # must be same character
                if grid[nx][ny] != ch:
                    continue

                # ignore edge back to immediate parent
                if nx == px and ny == py:
                    continue

                # if we see a visited same-char neighbor that's not parent -> cycle
                if visited[nx][ny]:
                    return True

                if dfs(nx, ny, x, y, ch):
                    return True

            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False
