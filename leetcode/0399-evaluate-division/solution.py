from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build the graph: graph[x][y] = x / y
        graph = defaultdict(dict)
        
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        
        def dfs(curr: str, target: str, visited: set) -> float:
            """Returns curr / target using DFS traversal."""
            if curr == target:
                return 1.0
            
            visited.add(curr)
            
            for neighbor, weight in graph[curr].items():
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1.0:
                        return weight * result
            
            return -1.0
        
        # Process all queries
        results = []
        for c, d in queries:
            if c not in graph or d not in graph:
                results.append(-1.0)
            elif c == d:
                results.append(1.0)
            else:
                results.append(dfs(c, d, set()))
        
        return results
