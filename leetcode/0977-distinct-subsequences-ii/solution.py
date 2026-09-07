class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # end[c] = number of distinct subsequences ending in character c
        end = [0] * 26
        total = 0

        for ch in s:
            idx = ord(ch) - ord('a')

            # Append ch to every existing subsequence, or start with ch.
            new_count = (total + 1) % MOD

            # Replace rather than add: all subsequences newly ending in ch
            # supersede the old set ending in ch, avoiding duplicates.
            total = (total + new_count - end[idx]) % MOD
            end[idx] = new_count

        return total
