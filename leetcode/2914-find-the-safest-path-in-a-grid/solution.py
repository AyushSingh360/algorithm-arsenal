from collections import deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        d = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    d[i][j] = 0
                    q.append((i, j))

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))

        pq = [(-d[0][0], 0, 0)]
        best = [[-1] * n for _ in range(n)]
        best[0][0] = d[0][0]

        while pq:
            val, x, y = heapq.heappop(pq)
            val = -val
            if x == n - 1 and y == n - 1:
                return val
            if val < best[x][y]:
                continue
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    nv = min(val, d[nx][ny])
                    if nv > best[nx][ny]:
                        best[nx][ny] = nv
                        heapq.heappush(pq, (-nv, nx, ny))
        return 0
