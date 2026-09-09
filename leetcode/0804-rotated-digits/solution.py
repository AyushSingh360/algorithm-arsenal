class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        from functools import lru_cache

        good = {0, 1, 2, 5, 6, 8, 9}
        change = {2, 5, 6, 9}  # must use at least one of these

        @lru_cache(None)
        def dp(pos: int, tight: int, diff: int) -> int:
            if pos == len(s):
                # diff=1 ⇒ used at least one changing digit
                return 1 if diff == 1 else 0

            limit = int(s[pos]) if tight else 9
            ans = 0

            for d in range(0, limit + 1):
                if d not in good:
                    continue
                ntight = tight and (d == limit)
                ndiff = diff or (d in change)
                ans += dp(pos + 1, int(ntight), int(ndiff))
            return ans

        # dp counts from 0..n; subtract the contribution of 0 explicitly.
        # For 0: all digits are 0 ⇒ diff = 0, so dp() already returns 0 for it.
        # So just return dp(0, 1, 0).
        return dp(0, 1, 0)
