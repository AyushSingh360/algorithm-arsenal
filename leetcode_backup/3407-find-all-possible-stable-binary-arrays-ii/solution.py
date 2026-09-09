class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7

        # dp0[i][j]: end with 0 using i zeros, j ones
        # dp1[i][j]: end with 1
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # base: empty -> we conceptually start from 0
        # first group can be zeros or ones
        for k in range(1, min(limit, zero) + 1):
            dp0[k][0] = 1
        for k in range(1, min(limit, one) + 1):
            dp1[0][k] = 1

        # prefix sums along zero dimension for dp1, and along one dimension for dp0
        # pref1[i][j] = sum_{t=0..i} dp1[t][j]
        # pref0[i][j] = sum_{t=0..j} dp0[i][t]
        pref1 = [[0] * (one + 1) for _ in range(zero + 1)]
        pref0 = [[0] * (one + 1) for _ in range(zero + 1)]

        # initialize prefix for base
        for i in range(zero + 1):
            for j in range(one + 1):
                if i == 0 and j == 0:
                    continue
                pref1[i][j] = ((pref1[i - 1][j] if i > 0 else 0) + dp1[i][j]) % MOD
                pref0[i][j] = ((pref0[i][j - 1] if j > 0 else 0) + dp0[i][j]) % MOD

        for i in range(zero + 1):
            for j in range(one + 1):
                if i == 0 and j == 0:
                    continue

                # transitions to end with 0: append a group of k zeros (1..limit) after something ending with 1
                if i > 0 and j > 0:
                    # sum dp1[i-k][j] for k = 1..min(limit, i)
                    lo = max(0, i - limit)
                    hi = i - 1
                    if hi >= 0:
                        total = pref1[hi][j]
                        if lo > 0:
                            total = (total - pref1[lo - 1][j]) % MOD
                        dp0[i][j] = (dp0[i][j] + total) % MOD

                # transitions to end with 1: append a group of k ones (1..limit) after something ending with 0
                if i > 0 and j > 0:
                    # sum dp0[i][j-k] for k = 1..min(limit, j)
                    lo = max(0, j - limit)
                    hi = j - 1
                    if hi >= 0:
                        total = pref0[i][hi]
                        if lo > 0:
                            total = (total - pref0[i][lo - 1]) % MOD
                        dp1[i][j] = (dp1[i][j] + total) % MOD

                # update prefixes after each cell
                pref1[i][j] = ((pref1[i - 1][j] if i > 0 else 0) + dp1[i][j]) % MOD
                pref0[i][j] = ((pref0[i][j - 1] if j > 0 else 0) + dp0[i][j]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD
