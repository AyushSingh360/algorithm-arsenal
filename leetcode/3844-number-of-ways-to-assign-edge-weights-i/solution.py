from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # Build adjacency list for the tree
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # DFS to compute depth of each node from root (node 1)
        def dfs(node: int, parent: int, depth: int) -> int:
            max_depth = depth
            for neighbor in adj[node]:
                if neighbor != parent:
                    max_depth = max(max_depth, dfs(neighbor, node, depth + 1))
            return max_depth
        
        # Find maximum depth from root
        max_depth = dfs(1, -1, 0)
        
        # The path from node 1 to any node at max_depth has exactly max_depth edges
        # For the total cost to be odd, we need an odd number of 1s along the path
        # Number of ways to choose odd count of 1s among max_depth edges = 2^(max_depth-1)
        
        MOD = 10**9 + 7
        return pow(2, max_depth - 1, MOD)
