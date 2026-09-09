from typing import List


class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        # top and bottom row indices of the k x k square
        top = x
        bottom = x + k - 1

        # swap rows within the submatrix vertically
        while top < bottom:
            # swap only the columns inside the submatrix: y to y + k - 1
            for col in range(y, y + k):
                grid[top][col], grid[bottom][col] = grid[bottom][col], grid[top][col]
            top += 1
            bottom -= 1

        return grid
