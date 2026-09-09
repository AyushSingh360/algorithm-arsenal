from typing import List


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1
        self.components -= 1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        must_edges = []
        optional_edges = []

        max_s = 0
        for u, v, s, must in edges:
            max_s = max(max_s, s)
            if must == 1:
                must_edges.append((u, v, s))
            else:
                optional_edges.append((u, v, s))

        def can(x: int) -> bool:
            dsu = DSU(n)

            # Mandatory edges must all be included, must not create cycle,
            # and cannot be upgraded, so each must already satisfy s >= x.
            for u, v, s in must_edges:
                if s < x:
                    return False
                if not dsu.union(u, v):
                    return False

            used_upgrades = 0

            # First use optional edges that already satisfy s >= x without upgrade.
            for u, v, s in optional_edges:
                if s >= x:
                    dsu.union(u, v)

            # Then use edges that can satisfy threshold only after one upgrade.
            for u, v, s in optional_edges:
                if s < x <= 2 * s:
                    if dsu.find(u) != dsu.find(v):
                        if used_upgrades == k:
                            break
                        dsu.union(u, v)
                        used_upgrades += 1

            return dsu.components == 1

        lo, hi = 0, 2 * max_s
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
