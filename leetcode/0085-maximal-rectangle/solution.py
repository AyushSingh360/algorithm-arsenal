from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        ans = 0

        def largestRectangleArea(heights: List[int]) -> int:
            stack = []  # will store indices
            max_area = 0
            # append a zero height sentinel
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            return max_area

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            ans = max(ans, largestRectangleArea(heights))

        return ans
