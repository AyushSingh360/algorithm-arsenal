from typing import List
from collections import defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # g: directed edges a -> b (actual invocation graph)
        # undirected: treat edges as undirected to propagate "cannot remove" info
        g = [[] for _ in range(n)]
        undirected = [[] for _ in range(n)]
        for a, b in invocations:
            g[a].append(b)
            undirected[a].append(b)
            undirected[b].append(a)

        # 1) DFS from k in directed graph -> mark all suspicious
        suspicious = [False] * n

        def dfs_susp(u: int) -> None:
            suspicious[u] = True
            for v in g[u]:
                if not suspicious[v]:
                    dfs_susp(v)

        dfs_susp(k)

        # 2) From every non-suspicious node, walk in undirected graph.
        # Any suspicious node reachable from outside cannot be removed,
        # so mark it back as non-suspicious.
        vis = [False] * n

        def dfs_rescue(u: int) -> None:
            vis[u] = True
            for v in undirected[u]:
                if not vis[v]:
                    # if we reach a suspicious node from outside, it must stay
                    if suspicious[v]:
                        suspicious[v] = False
                    dfs_rescue(v)

        for i in range(n):
            if not suspicious[i] and not vis[i]:
                dfs_rescue(i)

        # Remaining methods are exactly those not suspicious after possible rescue
        return [i for i in range(n) if not suspicious[i]]
