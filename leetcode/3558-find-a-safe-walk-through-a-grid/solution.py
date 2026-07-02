from collections import deque
from itertools import pairwise
from math import inf
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        # dist[i][j] = minimum number of unsafe cells (1s) to reach (i, j)
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        q = deque([(0, 0)])
        # directions encoded for pairwise: (up, right, down, left)
        dirs = (-1, 0, 1, 0, -1)

        while q:
            x, y = q.popleft()
            for dx, dy in pairwise(dirs):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = dist[x][y] + grid[nx][ny]
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        q.append((nx, ny))

        # We need health - cost >= 1  =>  cost <= health - 1  =>  cost < health
        return dist[m - 1][n - 1] < health
