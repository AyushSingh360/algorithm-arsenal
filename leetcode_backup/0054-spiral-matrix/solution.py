class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        while matrix:
            # 1. Add the top row
            result += matrix.pop(0)

            # 2. Add the last element of each remaining row
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            # 3. Add the bottom row in reverse
            if matrix:
                result += matrix.pop()[::-1]

            # 4. Add the first element of each remaining row (bottom to top)
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result
