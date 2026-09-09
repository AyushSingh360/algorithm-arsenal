from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs[0])  # number of columns
        n = len(strs)  # number of rows

        # dp[i] = length of longest valid column subsequence ending at column i
        dp = [1] * m

        for i in range(m):
            for j in range(i):
                # Check if we can place column i after column j
                ok = True
                for r in range(n):
                    if strs[r][j] > strs[r][i]:
                        ok = False
                        break
                if ok:
                    dp[i] = max(dp[i], dp[j] + 1)

        # max(dp) = max number of columns we can keep
        return m - max(dp)
