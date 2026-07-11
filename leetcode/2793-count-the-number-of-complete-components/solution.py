from typing import List
from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        complete_count = 0

        for start in range(n):
            if visited[start]:
                continue

            # BFS/DFS to get all vertices in this component
            queue = deque([start])
            visited[start] = True
            component_nodes = []

            while queue:
                node = queue.popleft()
                component_nodes.append(node)
                for nei in adj[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)

            # Now we have one connected component: component_nodes
            k = len(component_nodes)

            # Count edges inside this component via degree sum
            degree_sum = 0
            for node in component_nodes:
                degree_sum += len(adj[node])

            # Undirected: each edge counted twice in degree_sum
            edge_count = degree_sum // 2

            # Check completeness: a complete graph with k vertices
            # has k * (k - 1) / 2 edges
            if edge_count == k * (k - 1) // 2:
                complete_count += 1

        return complete_count
