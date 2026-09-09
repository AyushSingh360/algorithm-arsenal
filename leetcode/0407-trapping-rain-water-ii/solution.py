class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        import heapq

        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        # Min-heap to store (height, row, col)
        heap = []
        visited = [[False] * n for _ in range(m)]

        # Add all boundary cells to the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        water = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_height = 0

        while heap:
            height, row, col = heapq.heappop(heap)
            max_height = max(max_height, height)

            # Check all 4 directions
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # If neighbor is lower, it can trap water
                    if heightMap[nr][nc] < max_height:
                        water += max_height - heightMap[nr][nc]
                    heapq.heappush(heap, (heightMap[nr][nc], nr, nc))

        return water
