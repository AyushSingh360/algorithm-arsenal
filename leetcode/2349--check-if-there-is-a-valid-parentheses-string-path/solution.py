class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        path_len = m + n - 1

        # A valid parentheses string must have even length.
        if path_len % 2 == 1:
            return False

        # The path must start with '(' and end with ')'.
        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        # dp[r][c] = set of valid unmatched-open counts after reaching (r, c).
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                delta = 1 if grid[r][c] == '(' else -1

                if r > 0:
                    for balance in dp[r - 1][c]:
                        new_balance = balance + delta
                        if new_balance >= 0:
                            dp[r][c].add(new_balance)

                if c > 0:
                    for balance in dp[r][c - 1]:
                        new_balance = balance + delta
                        if new_balance >= 0:
                            dp[r][c].add(new_balance)

        return 0 in dp[-1][-1]
