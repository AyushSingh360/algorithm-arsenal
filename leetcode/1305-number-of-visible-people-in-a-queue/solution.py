class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        res = [0] * n
        stack = []  # will store heights of people to the right, monotonic decreasing

        # iterate from right to left
        for i in range(n - 1, -1, -1):
            visible = 0

            # pop all shorter people: each popped one is visible
            while stack and stack[-1] < heights[i]:
                stack.pop()
                visible += 1

            # if there is someone left on stack, they are taller/equal and visible,
            # but they block further view
            if stack:
                visible += 1

            res[i] = visible
            stack.append(heights[i])

        return res
