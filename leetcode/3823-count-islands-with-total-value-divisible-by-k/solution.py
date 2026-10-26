from collections import deque
from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                total = grid[i][j]
                grid[i][j] = 0
                q = deque([(i, j)])

                while q:
                    r, c = q.popleft()

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0:
                            total += grid[nr][nc]
                            grid[nr][nc] = 0
                            q.append((nr, nc))

                if total % k == 0:
                    ans += 1

        return ans
