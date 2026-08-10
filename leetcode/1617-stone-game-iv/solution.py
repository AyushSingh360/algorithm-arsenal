class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] = whether the current player can win with i stones
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                # If removing j² leaves the opponent a losing state,
                # then the current state is winning.
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1

        return dp[n]
