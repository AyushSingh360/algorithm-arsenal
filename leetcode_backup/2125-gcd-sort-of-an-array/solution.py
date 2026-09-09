from typing import List
from collections import defaultdict


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        max_num = max(nums)
        # smallest prime factor sieve
        spf = list(range(max_num + 1))
        p = 2
        while p * p <= max_num:
            if spf[p] == p:
                for x in range(p * p, max_num + 1, p):
                    if spf[x] == x:
                        spf[x] = p
            p += 1

        def factorize(x: int) -> List[int]:
            res = set()
            while x > 1:
                f = spf[x]
                res.add(f)
                while x % f == 0:
                    x //= f
            return list(res)

        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx

        # union each number with its prime factors
        for x in nums:
            for f in factorize(x):
                union(x, f)

        sorted_nums = sorted(nums)

        for a, b in zip(nums, sorted_nums):
            if a != b and find(a) != find(b):
                return False
        return True
