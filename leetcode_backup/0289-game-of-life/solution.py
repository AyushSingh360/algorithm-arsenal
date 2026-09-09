from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def live_neighbors(r: int, c: int) -> int:
            cnt = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        # Original live cells are 1 or 2 (1->0 we mark as 2)
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            cnt += 1
            return cnt

        # First pass: encode transitions
        # 0 -> 1: mark as 3
        # 1 -> 0: mark as 2
        for r in range(m):
            for c in range(n):
                ln = live_neighbors(r, c)

                if board[r][c] == 1:
                    if ln < 2 or ln > 3:
                        board[r][c] = 2  # live to dead
                else:  # board[r][c] == 0
                    if ln == 3:
                        board[r][c] = 3  # dead to live

        # Second pass: finalize to 0 or 1
        for r in range(m):
            for c in range(n):
                if board[r][c] == 1 or board[r][c] == 3:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
