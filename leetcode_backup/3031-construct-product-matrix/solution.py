from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        k = n * m

        a = [0] * k
        idx = 0
        for i in range(n):
            for j in range(m):
                a[idx] = grid[i][j] % MOD
                idx += 1

        pref = [1] * (k + 1)
        for i in range(k):
            pref[i + 1] = (pref[i] * a[i]) % MOD

        suff = [1] * (k + 1)
        for i in range(k - 1, -1, -1):
            suff[i] = (suff[i + 1] * a[i]) % MOD

        res_flat = [0] * k
        for i in range(k):
            res_flat[i] = (pref[i] * suff[i + 1]) % MOD

        ans = [[0] * m for _ in range(n)]
        idx = 0
        for i in range(n):
            for j in range(m):
                ans[i][j] = res_flat[idx]
                idx += 1

        return ans
