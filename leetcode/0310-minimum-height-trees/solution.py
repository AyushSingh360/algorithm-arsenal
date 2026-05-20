class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [i for i in range(n) if len(graph[i]) == 1]

        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                nei = graph[leaf].pop()
                graph[nei].remove(leaf)
                if len(graph[nei]) == 1:
                    new_leaves.append(nei)

            leaves = new_leaves

        return leaves
