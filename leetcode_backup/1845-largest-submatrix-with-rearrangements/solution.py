class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        for row in matrix:
            for j in range(n):
                if row[j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            sorted_heights = sorted(heights, reverse=True)
            for j in range(n):
                area = sorted_heights[j] * (j + 1)
                if area > max_area:
                    max_area = area

        return max_area
