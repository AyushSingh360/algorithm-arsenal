from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        # Track who knows the secret
        knows = [False] * n
        knows[0] = True
        knows[firstPerson] = True

        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])

        i = 0
        m = len(meetings)

        while i < m:
            # Group all meetings with the same time
            t = meetings[i][2]
            j = i
            while j < m and meetings[j][2] == t:
                j += 1

            # Build graph for this time slice
            adj = defaultdict(list)
            people = set()
            for k in range(i, j):
                x, y, _ = meetings[k]
                adj[x].append(y)
                adj[y].append(x)
                people.add(x)
                people.add(y)

            # Multi-source BFS from all people in this slice who already know the secret
            q = deque()
            for p in people:
                if knows[p]:
                    q.append(p)

            visited = set(q)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        # Only now does v know the secret
                        if knows[u]:
                            knows[v] = True
                        q.append(v)

            # Important: we only keep `knows` updated; people who
            # didn't connect to any knower in this slice remain False.

            i = j

        # Collect all people who know the secret
        return [i for i in range(n) if knows[i]]
