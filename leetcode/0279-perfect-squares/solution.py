class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] = least number of perfect squares that sum to i
        dp = [0] + [float("inf")] * n

        # precompute all perfect squares <= n
        squares = []
        k = 1
        while k * k <= n:
            squares.append(k * k)
            k += 1

        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)

        return dp[n]
