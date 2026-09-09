from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1  # start at top-right

        while r < rows and c >= 0:
            val = matrix[r][c]
            if val == target:
                return True
            elif val > target:
                # current value too big, move left to smaller values
                c -= 1
            else:
                # current value too small, move down to larger values
                r += 1

        return False
