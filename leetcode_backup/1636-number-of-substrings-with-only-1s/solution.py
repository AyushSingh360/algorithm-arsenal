class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        cur = 0  # current consecutive '1's

        for ch in s:
            if ch == "1":
                cur += 1
                ans += cur
            else:
                cur = 0

        return ans % MOD
