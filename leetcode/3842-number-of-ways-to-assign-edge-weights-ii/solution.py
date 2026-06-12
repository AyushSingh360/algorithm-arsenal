from typing import List
import sys
sys.setrecursionlimit(1_000_000)

MOD = 10**9 + 7

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        # Build adjacency list
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = (n).bit_length()
        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        # DFS to fill depth and immediate parent
        from collections import deque
        root = 1
        depth[root] = 0
        parent[0][root] = 0
        q = deque([root])
        visited = [False] * (n + 1)
        visited[root] = True

        while q:
            u = q.popleft()
            for v in g[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[0][v] = u
                    q.append(v)

        # Binary lifting table
        for k in range(1, LOG):
            for v in range(1, n + 1):
                p = parent[k - 1][v]
                parent[k][v] = parent[k - 1][p] if p else 0

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            # Lift u up to depth v
            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = parent[bit][u]
                diff >>= 1
                bit += 1
            if u == v:
                return u
            # Lift both up until parents match
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        # Precompute powers of 2
        maxLen = n  # max path length in a tree with n nodes is at most n-1
        pow2 = [1] * (maxLen + 1)
        for i in range(1, maxLen + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            w = lca(u, v)
            L = depth[u] + depth[v] - 2 * depth[w]
            # number of ways to get odd sum on a path of length L is 2^(L-1)
            ans.append(pow2[L - 1])
        return ans
