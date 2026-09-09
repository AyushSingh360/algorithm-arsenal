from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # Optional pruning: if word has more of some char than board, impossible
        from collections import Counter

        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)
        for ch, cnt in word_count.items():
            if board_count[ch] < cnt:
                return False

        def dfs(i: int, j: int, k: int) -> bool:
            # k is index in word we need to match at (i, j)
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[k]:
                return False

            # Mark as visited
            tmp = board[i][j]
            board[i][j] = "#"

            # Explore 4 directions
            found = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )

            # Backtrack
            board[i][j] = tmp
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
