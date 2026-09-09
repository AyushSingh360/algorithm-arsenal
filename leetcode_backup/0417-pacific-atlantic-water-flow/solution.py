class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        # Sets to track which cells can reach each ocean
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, visited, prev_height):
            # Base cases: out of bounds, already visited, or water can't flow
            if (
                r < 0
                or r >= m
                or c < 0
                or c >= n
                or (r, c) in visited
                or heights[r][c] < prev_height
            ):
                return

            visited.add((r, c))

            # Explore all 4 directions
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Start DFS from Pacific edges (top row and left column)
        for c in range(n):
            dfs(0, c, pacific_reachable, heights[0][c])
        for r in range(m):
            dfs(r, 0, pacific_reachable, heights[r][0])

        # Start DFS from Atlantic edges (bottom row and right column)
        for c in range(n):
            dfs(m - 1, c, atlantic_reachable, heights[m - 1][c])
        for r in range(m):
            dfs(r, n - 1, atlantic_reachable, heights[r][n - 1])

        # Find cells that can reach both oceans
        result = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])

        return result
