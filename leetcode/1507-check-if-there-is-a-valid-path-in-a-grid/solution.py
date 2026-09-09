from collections import deque
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # If start == end, single cell is always valid
        if m == 1 and n == 1:
            return True

        # For each type, list of possible moves: (dx, dy)
        moves = {
            1: [(0, -1), (0, 1)],  # left, right
            2: [(-1, 0), (1, 0)],  # up, down
            3: [(0, -1), (1, 0)],  # left, down
            4: [(0, 1), (1, 0)],  # right, down
            5: [(0, -1), (-1, 0)],  # left, up
            6: [(0, 1), (-1, 0)],  # right, up
        }

        # For a direction (dx, dy), which types can connect *into* from that side
        need_from = {
            (0, -1): [
                1,
                4,
                6,
            ],  # we moved left -> neighbor is to the left; it needs opening on its right
            (0, 1): [
                1,
                3,
                5,
            ],  # we moved right -> neighbor is to the right; it needs opening on its left
            (-1, 0): [
                2,
                3,
                4,
            ],  # we moved up   -> neighbor is above; it needs opening on its bottom
            (1, 0): [
                2,
                5,
                6,
            ],  # we moved down -> neighbor is below; it needs opening on its top
        }

        q = deque([(0, 0)])
        vis = [[False] * n for _ in range(m)]
        vis[0][0] = True

        while q:
            x, y = q.popleft()
            if x == m - 1 and y == n - 1:
                return True

            t = grid[x][y]
            for dx, dy in moves[t]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny]:
                    # Check if neighbor has a compatible entrance
                    if grid[nx][ny] in need_from[(dx, dy)]:
                        vis[nx][ny] = True
                        q.append((nx, ny))

        return False
