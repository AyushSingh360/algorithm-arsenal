class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # same: patterns like ABA (two colors)
        # diff: patterns like ABC (three distinct colors)
        same = 6
        diff = 6

        for _ in range(n - 1):
            next_same = (same * 3 + diff * 2) % MOD
            next_diff = (same * 2 + diff * 2) % MOD
            same, diff = next_same, next_diff

        return (same + diff) % MOD
