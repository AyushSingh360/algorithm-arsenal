from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            elems = []
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer

            # 1) Extract the current layer into a list in traversal order

            # top row (left → right)
            for j in range(left, right):
                elems.append(grid[top][j])
            # right column (top → bottom)
            for i in range(top, bottom):
                elems.append(grid[i][right])
            # bottom row (right → left)
            for j in range(right, left, -1):
                elems.append(grid[bottom][j])
            # left column (bottom → top)
            for i in range(bottom, top, -1):
                elems.append(grid[i][left])

            # 2) Compute effective rotations (counter-clockwise)
            L = len(elems)
            r = k % L
            if r:
                # rotate left by r: [r:] + [:r]
                rotated = elems[r:] + elems[:r]
            else:
                rotated = elems

            # 3) Write back rotated values in the same traversal order
            idx = 0

            # top row (left → right)
            for j in range(left, right):
                grid[top][j] = rotated[idx]
                idx += 1
            # right column (top → bottom)
            for i in range(top, bottom):
                grid[i][right] = rotated[idx]
                idx += 1
            # bottom row (right → left)
            for j in range(right, left, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1
            # left column (bottom → top)
            for i in range(bottom, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1

        return grid
