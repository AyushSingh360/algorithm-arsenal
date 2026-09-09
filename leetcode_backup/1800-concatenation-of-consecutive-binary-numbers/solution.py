class Solution(object):
    def concatenatedBinary(self, n):
        MOD = 10**9 + 7
        ans = 0
        bits = 0

        for i in range(1, n + 1):
            # If i is a power of 2, increase bit-length
            if (i & (i - 1)) == 0:
                bits += 1

            ans = ((ans << bits) + i) % MOD

        return ans
