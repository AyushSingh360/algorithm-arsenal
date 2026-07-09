from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)

        # 1. Collect positions and values of non-zero digits.
        pos = []
        vals = []
        for i, ch in enumerate(s):
            if ch != "0":
                pos.append(i)
                vals.append(int(ch))

        k = len(vals)
        if k == 0:
            # String has no non-zero digits at all, all answers are 0.
            return [0] * len(queries)

        # 2. Build prefix-sum of digits and prefix "concatenation" values for x.
        pref_sum = [0] * (k + 1)  # sum of digits
        pref_x = [0] * (k + 1)  # number formed by concatenation
        pow10 = [1] * (k + 1)  # powers of 10 for modulo

        for i in range(1, k + 1):
            pref_sum[i] = (pref_sum[i - 1] + vals[i - 1]) % MOD
            pref_x[i] = (pref_x[i - 1] * 10 + vals[i - 1]) % MOD
            pow10[i] = (pow10[i - 1] * 10) % MOD

        def get_range_indices(l: int, r: int):
            # First non-zero digit index >= l
            left_idx = bisect_left(pos, l)
            # Last non-zero digit index <= r
            right_idx = bisect_right(pos, r) - 1
            if left_idx > right_idx:
                return None
            # Convert to 1-based for our prefix arrays
            return left_idx + 1, right_idx + 1

        ans = []
        for l, r in queries:
            idx_range = get_range_indices(l, r)
            if idx_range is None:
                ans.append(0)
                continue

            L, R = idx_range
            # 3. Extract x from pref_x using modular arithmetic.
            length = R - L + 1
            # x = number formed by vals[L-1..R-1]
            total = pref_x[R]
            prefix = pref_x[L - 1] * pow10[length] % MOD
            x = (total - prefix) % MOD

            # 4. Sum of digits in x from pref_sum.
            digit_sum = (pref_sum[R] - pref_sum[L - 1]) % MOD

            ans.append((x * digit_sum) % MOD)

        return ans
