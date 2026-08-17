class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i == j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0

            for p in range(i, j):
                leftSum = prefix[p + 1] - prefix[i]
                rightSum = prefix[j + 1] - prefix[p + 1]

                if leftSum < rightSum:
                    # Right is removed, Alice keeps LEFT
                    ans = max(ans, leftSum + solve(i, p))

                elif leftSum > rightSum:
                    # Left is removed, Alice keeps RIGHT
                    ans = max(ans, rightSum + solve(p + 1, j))

                else:
                    # Equal -> Alice chooses either side
                    ans = max(
                        ans,
                        leftSum + solve(i, p),
                        rightSum + solve(p + 1, j)
                    )

            dp[i][j] = ans
            return ans

        return solve(0, n - 1)
