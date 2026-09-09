class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        # Length check
        if m + n != len(s3):
            return False

        # dp[i][j] = can s3[:i+j] be formed by interleaving s1[:i] and s2[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # First row: s1 empty, only s2 used
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # First column: s2 empty, only s1 used
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # Fill the rest
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = i + j - 1
                from_s1 = dp[i - 1][j] and s1[i - 1] == s3[k]
                from_s2 = dp[i][j - 1] and s2[j - 1] == s3[k]
                dp[i][j] = from_s1 or from_s2

        return dp[m][n]
