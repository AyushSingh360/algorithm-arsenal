from typing import List


class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] += 1
        return True


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        pos = [0] * n
        for i, idx in enumerate(order):
            pos[idx] = i

        # Build edges only between consecutive sorted values while the gap is valid.
        # This is enough to preserve connectivity structure, and for distance we
        # use the jump forest below.
        nxt = [i for i in range(n)]
        dsu = DSU(n)

        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and nums[order[j + 1]] - nums[order[i]] <= maxDiff:
                dsu.union(order[j], order[j + 1])
                j += 1

        # Build the "jump to farthest reachable" parent in sorted order.
        # parent[i] = farthest index reachable in one jump from sorted position i.
        parent = [i for i in range(n)]
        r = 0
        for l in range(n):
            if r < l:
                r = l
            while r + 1 < n and nums[order[r + 1]] - nums[order[l]] <= maxDiff:
                r += 1
            parent[l] = r

        LOG = (n).bit_length()
        up = [parent[:]]
        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        def steps_between(a, b):
            # a, b are original indices
            if a == b:
                return 0
            if dsu.find(a) != dsu.find(b):
                return -1

            ia, ib = pos[a], pos[b]
            if ia > ib:
                ia, ib = ib, ia

            # Minimum jumps from ia to ib using binary lifting on parent pointers
            cur = ia
            ans = 0
            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < ib:
                    cur = up[k][cur]
                    ans += 1 << k
            if cur < ib:
                ans += 1
            return ans

        return [steps_between(u, v) for u, v in queries]
