import heapq


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        # Use Dijkstra's algorithm with min-heap
        # Each element in heap: (max_elevation_so_far, row, col)
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while heap:
            time, row, col = heapq.heappop(heap)

            # If we reached the bottom-right corner
            if row == n - 1 and col == n - 1:
                return time

            # Explore all 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check bounds and if already visited
                if (
                    0 <= new_row < n
                    and 0 <= new_col < n
                    and (new_row, new_col) not in visited
                ):

                    visited.add((new_row, new_col))
                    # The time needed is the max of current time and new cell's elevation
                    new_time = max(time, grid[new_row][new_col])
                    heapq.heappush(heap, (new_time, new_row, new_col))

        return -1  # Should never reach here
