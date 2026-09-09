from collections import defaultdict, Counter
from typing import List


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1


class Solution:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        n = len(source)
        dsu = DSU(n)

        # 1. Build connected components via DSU
        for a, b in allowedSwaps:
            dsu.union(a, b)

        # 2. For each component root, store freq of source values
        comp_freq = defaultdict(Counter)
        for i, val in enumerate(source):
            root = dsu.find(i)
            comp_freq[root][val] += 1

        # 3. For each index, try to match target value inside its component
        ans = 0
        for i, val in enumerate(target):
            root = dsu.find(i)
            if comp_freq[root][val] > 0:
                comp_freq[root][val] -= 1
            else:
                ans += 1

        return ans
