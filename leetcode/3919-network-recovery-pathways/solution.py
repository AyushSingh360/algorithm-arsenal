from typing import List
from collections import deque, defaultdict
import math


class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n = len(online)
        if n == 0:
            return -1

        # Build graph and indegrees for topo sort
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        costs = set()

        for u, v, c in edges:
            graph[u].append((v, c))
            indeg[v] += 1
            costs.add(c)

        # Edge case: no edges
        if not edges:
            return 0 if 0 == n - 1 and k >= 0 else -1

        # Topological order (Kahn's algorithm)
        topo = []
        dq = deque(i for i in range(n) if indeg[i] == 0)
        while dq:
            u = dq.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    dq.append(v)

        # If topo does not contain all nodes, graph wasn't a DAG (but constraints say it is)
        if len(topo) < n:
            return -1

        # Sort distinct costs for binary search over them
        sorted_costs = sorted(costs)
        if not sorted_costs:
            return -1

        def can_achieve(threshold: int) -> bool:
            # DP over topo order with only edges of cost >= threshold
            INF = math.inf
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue
                # Node must be online or be endpoint (0 or n-1)
                if u not in (0, n - 1) and not online[u]:
                    continue
                for v, c in graph[u]:
                    if c < threshold:
                        continue
                    # Intermediate node must be online
                    if v not in (0, n - 1) and not online[v]:
                        continue
                    new_cost = dist[u] + c
                    if new_cost < dist[v]:
                        dist[v] = new_cost

            return dist[n - 1] <= k

        # Binary search over sorted_costs
        lo, hi = 0, len(sorted_costs) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            val = sorted_costs[mid]
            if can_achieve(val):
                ans = val
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
