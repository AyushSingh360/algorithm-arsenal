class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return

        m, n = len(matrix), len(matrix[0])
        # prefix[i][j] = sum of elements in rectangle (0,0) to (i-1, j-1)
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                self.prefix[i + 1][j + 1] = (
                    self.prefix[i][j + 1]  # above
                    + self.prefix[i + 1][j]  # left
                    - self.prefix[i][j]  # overlap
                    + matrix[i][j]  # current cell
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Inclusion–exclusion on the prefix matrix
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )
