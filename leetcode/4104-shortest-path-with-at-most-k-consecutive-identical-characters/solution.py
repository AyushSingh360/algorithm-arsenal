
import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:

        # Step 1: Build adjacency list
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # Step 2: Initialize distance array
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Step 3: Initialize starting state
        dist[0][1] = 0

        # Priority queue: (cost, node, consecutive_count)
        pq = [(0, 0, 1)]

        # Step 4: Dijkstra's algorithm
        while pq:

            cost, u, count = heapq.heappop(pq)

            # Skip outdated states
            if cost != dist[u][count]:
                continue

            # Destination reached
            if u == n - 1:
                return cost

            # Explore adjacent nodes
            for v, w in graph[u]:

                # Calculate consecutive character count
                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                # Skip invalid paths
                if new_count > k:
                    continue

                # Calculate new cost
                new_cost = cost + w

                # Relaxation
                if new_cost < dist[v][new_count]:

                    dist[v][new_count] = new_cost

                    heapq.heappush(
                        pq,
                        (new_cost, v, new_count)
                    )

        # No valid path exists
        return -1

