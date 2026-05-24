from functools import lru_cache
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dfs(i: int) -> int:
            # max indices we can visit starting at i (including i)
            best = 1

            # look left
            step = 1
            while step <= d and i - step >= 0:
                j = i - step
                if arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))
                step += 1

            # look right
            step = 1
            while step <= d and i + step < n:
                j = i + step
                if arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))
                step += 1

            return best

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans
