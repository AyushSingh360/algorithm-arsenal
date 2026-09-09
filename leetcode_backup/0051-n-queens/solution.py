class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [["."] * n for _ in range(n)]

        def is_safe(row, col):
            for i in range(row):
                if board[i][col] == "Q":
                    return False
                if col - (row - i) >= 0 and board[i][col - (row - i)] == "Q":
                    return False
                if col + (row - i) < n and board[i][col + (row - i)] == "Q":
                    return False
            return True

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        backtrack(0)
        return res
