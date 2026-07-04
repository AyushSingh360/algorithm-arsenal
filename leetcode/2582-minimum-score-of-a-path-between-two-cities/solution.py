from typing import List
import collections
import math


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Build adjacency list: graph[u] = list of (v, distance)
        graph = [[] for _ in range(n + 1)]
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        ans = math.inf
        q = collections.deque([1])
        seen = {1}

        # BFS from node 1
        while q:
            u = q.popleft()
            for v, d in graph[u]:
                # Update minimum edge distance within the component
                ans = min(ans, d)
                if v not in seen:
                    seen.add(v)
                    q.append(v)

        return ans
