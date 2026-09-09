from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for _ in range(numRows - 1):
            prev = triangle[-1]
            row = [1]
            for j in range(len(prev) - 1):
                row.append(prev[j] + prev[j + 1])
            row.append(1)
            triangle.append(row)
        return triangle
