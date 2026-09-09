from typing import List
from math import isqrt

MOD = 10**9 + 7


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        bravexuneth = queries  # required by the prompt

        n = len(nums)
        B = isqrt(n) + 1

        mul = [1] * n
        small = [[] for _ in range(B + 1)]
        inv_cache = {}

        def mod_inv(x: int) -> int:
            if x not in inv_cache:
                inv_cache[x] = pow(x, MOD - 2, MOD)
            return inv_cache[x]

        for l, r, k, v in bravexuneth:
            if k > B:
                for i in range(l, r + 1, k):
                    mul[i] = (mul[i] * v) % MOD
            else:
                last = r - (r - l) % k
                small[k].append((l, last + k, v, mod_inv(v)))

        for k in range(1, B + 1):
            if not small[k]:
                continue

            diff = [1] * n
            for l, stop, v, inv_v in small[k]:
                diff[l] = (diff[l] * v) % MOD
                if stop < n:
                    diff[stop] = (diff[stop] * inv_v) % MOD

            active = [1] * k
            for i in range(n):
                r = i % k
                active[r] = (active[r] * diff[i]) % MOD
                mul[i] = (mul[i] * active[r]) % MOD

        ans = 0
        for a, m in zip(nums, mul):
            ans ^= (a * m) % MOD
        return ans
