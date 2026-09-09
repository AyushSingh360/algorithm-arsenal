class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows = len(mat)
        cols = len(mat[0])
        count = 0

        # Precompute row sums and column sums
        row_sums = [sum(mat[i]) for i in range(rows)]
        col_sums = [sum(mat[i][j] for i in range(rows)) for j in range(cols)]

        # Check each position
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    count += 1

        return count
