from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list and indegree array
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        # Start with all courses having no prerequisites
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        # Standard Kahn's algorithm
        while q:
            course = q.popleft()
            order.append(course)

            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # If we processed all courses, return order; otherwise there is a cycle
        return order if len(order) == numCourses else []
