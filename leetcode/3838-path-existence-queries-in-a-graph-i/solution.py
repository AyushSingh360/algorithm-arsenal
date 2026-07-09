from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:
        # comp[i] = component id of node i
        comp = [0] * n

        # Build components in one linear pass
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                comp[i] = comp[i - 1]
            else:
                comp[i] = comp[i - 1] + 1

        # Answer queries: same component => path exists
        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])

        return ans
