from typing import List
import sys

sys.setrecursionlimit(1_000_000)


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build adjacency: (neighbor, cost)
        # cost = 0 if edge is u -> v (no reversal needed when going u→v)
        # cost = 1 if we must reverse it to go that way from parent
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append((v, 0))  # original direction u -> v
            g[v].append((u, 1))  # to go v -> u we need one reversal

        ans = [0] * n

        # DFS1: total reversals needed so that every node is reachable from 0
        def dfs1(u: int, p: int) -> int:
            total = 0
            for v, cost in g[u]:
                if v == p:
                    continue
                total += cost + dfs1(v, u)
            return total

        ans[0] = dfs1(0, -1)

        # DFS2: reroot DP to compute answer for all roots
        def dfs2(u: int, p: int):
            for v, cost in g[u]:
                if v == p:
                    continue
                if cost == 0:
                    # edge u->v: when root moves from u to v, we "lose" a good direction,
                    # so need one more reversal
                    ans[v] = ans[u] + 1
                else:
                    # edge v->u originally (we stored as cost=1 for u->v),
                    # when root moves to v, this edge direction becomes good, so one less
                    ans[v] = ans[u] - 1
                dfs2(v, u)

        dfs2(0, -1)
        return ans
