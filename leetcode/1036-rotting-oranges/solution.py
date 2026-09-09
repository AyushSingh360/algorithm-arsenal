from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0

        # initialize queue with all initially rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # if no fresh oranges, time is 0
        if fresh == 0:
            return 0

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS level by level
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
            minutes += 1

        # if there are still fresh oranges, it's impossible
        return minutes if fresh == 0 else -1
