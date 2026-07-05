class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        # dp[i][j] = max score from (i, j) to 'S'
        # cnt[i][j] = number of paths achieving dp[i][j]
        dp = [[-1] * n for _ in range(n)]
        cnt = [[0] * n for _ in range(n)]

        # Start cell 'S' (bottom-right)
        dp[n - 1][n - 1] = 0
        cnt[n - 1][n - 1] = 1

        # Fill from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X':
                    dp[i][j] = -1
                    cnt[i][j] = 0
                    continue

                # skip 'S' (already initialized)
                if i == n - 1 and j == n - 1:
                    continue

                best = -1
                ways = 0

                # We can come to (i, j) from (i+1, j), (i, j+1), (i+1, j+1)
                for x, y in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if 0 <= x < n and 0 <= y < n and dp[x][y] != -1:
                        if dp[x][y] > best:
                            best = dp[x][y]
                            ways = cnt[x][y]
                        elif dp[x][y] == best:
                            ways = (ways + cnt[x][y]) % MOD

                if best == -1:
                    dp[i][j] = -1
                    cnt[i][j] = 0
                    continue

                # Add numeric value if current cell is a digit
                if board[i][j].isdigit():
                    best = (best + int(board[i][j])) % MOD

                dp[i][j] = best
                cnt[i][j] = ways % MOD

        # 'E' is at (0, 0)
        if dp[0][0] == -1:
            return [0, 0]
        return [dp[0][0] % MOD, cnt[0][0] % MOD]
