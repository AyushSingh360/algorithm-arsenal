from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r0, c0 = click

        # If click is on a mine, game over
        if board[r0][c0] == "M":
            board[r0][c0] = "X"
            return board

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        def dfs(r: int, c: int) -> None:
            # Only process unrevealed empty cells
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != "E":
                return

            # Count adjacent mines
            mine_count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "M":
                    mine_count += 1

            if mine_count == 0:
                # No adjacent mines: mark blank and recurse on neighbors
                board[r][c] = "B"
                for dr, dc in directions:
                    dfs(r + dr, c + dc)
            else:
                # Has adjacent mines: set digit and stop
                board[r][c] = str(mine_count)

        dfs(r0, c0)
        return board
