from typing import List


class Solution:
    def palindromePath(
        self, n: int, edges: List[List[int]], s: str, queries: List[str]
    ) -> List[bool]:

        # 1. Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()

        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n

        # 2. Iterative DFS: Euler tour and parent information
        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1

                parent[0][u] = u if p == -1 else p

                stack.append((u, p, 1))

                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        # 3. Binary lifting table
        for k in range(1, LOG):
            for u in range(n):
                parent[k][u] = parent[k - 1][parent[k - 1][u]]

        # 4. Lowest Common Ancestor
        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            k = 0

            while diff:
                if diff & 1:
                    u = parent[k][u]
                diff >>= 1
                k += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        # 5. Fenwick tree with XOR operations
        class Fenwick:
            def __init__(self, size):
                self.size = size
                self.bit = [0] * (size + 1)

            def update(self, i: int, val: int) -> None:
                i += 1
                while i <= self.size:
                    self.bit[i] ^= val
                    i += i & -i

            def query(self, i: int) -> int:
                result = 0
                i += 1

                while i > 0:
                    result ^= self.bit[i]
                    i -= i & -i

                return result

        # 6. Character masks
        chars = [1 << (ord(c) - ord("a")) for c in s]

        bit = Fenwick(n)

        def range_xor(left: int, right: int, val: int) -> None:
            bit.update(left, val)

            if right + 1 < n:
                bit.update(right + 1, val)

        # IMPORTANT: Initialize using each NODE'S character mask.
        # Every node contributes to the root-prefix masks of its subtree.
        for u in range(n):
            range_xor(tin[u], tout[u], chars[u])

        # 7. Process queries
        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                new_mask = 1 << (ord(c) - ord("a"))
                delta = chars[u] ^ new_mask

                if delta:
                    range_xor(tin[u], tout[u], delta)
                    chars[u] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])

                # Root-to-node prefix masks
                pu = bit.query(tin[u])
                pv = bit.query(tin[v])

                # Lowest common ancestor
                w = lca(u, v)

                # Mask of the complete path, including both endpoints
                path_mask = pu ^ pv ^ chars[w]

                # At most one character may have an odd frequency
                ans.append(path_mask == 0 or (path_mask & (path_mask - 1)) == 0)

        return ans
