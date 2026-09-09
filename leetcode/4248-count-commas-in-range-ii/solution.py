class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        start = 1_000
        commas = 1

        while start <= n:
            end = start * 1_000 - 1
            count = min(n, end) - start + 1
            ans += count * commas

            start *= 1_000
            commas += 1

        return ans
