class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []  # indices, heights increasing
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            curr_h = heights[i] if i < n else 0
            while stack and curr_h < heights[stack[-1]]:
                h = heights[stack.pop()]
                left_idx = stack[-1] if stack else -1
                width = i - left_idx - 1
                max_area = max(max_area, h * width)
            stack.append(i)

        return max_area
