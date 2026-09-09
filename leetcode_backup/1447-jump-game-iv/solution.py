from collections import deque, defaultdict
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        same = defaultdict(list)
        for i, v in enumerate(arr):
            same[v].append(i)
        q = deque([0])
        dist = [-1] * n
        dist[0] = 0
        while q:
            i = q.popleft()
            d = dist[i]
            for j in (i - 1, i + 1):
                if 0 <= j < n and dist[j] == -1:
                    dist[j] = d + 1
                    q.append(j)
            for j in same[arr[i]]:
                if dist[j] == -1:
                    dist[j] = d + 1
                    q.append(j)
            same[arr[i]].clear()
        return dist[n - 1]
