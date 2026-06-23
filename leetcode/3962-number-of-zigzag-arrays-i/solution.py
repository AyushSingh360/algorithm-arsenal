class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # Length 2 initialization:
        # up[y]   = count of pairs (x, y) with x < y
        # down[y] = count of pairs (x, y) with x > y
        up = [i % MOD for i in range(m)]
        down = [(m - 1 - i) % MOD for i in range(m)]

        for _ in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m

            pref_down = [0] * (m + 1)
            for i in range(m):
                pref_down[i + 1] = (pref_down[i] + down[i]) % MOD

            pref_up = [0] * (m + 1)
            for i in range(m):
                pref_up[i + 1] = (pref_up[i] + up[i]) % MOD

            total_up = pref_up[m]

            for y in range(m):
                new_up[y] = pref_down[y]                # sum of down[x] for x < y
                new_down[y] = (total_up - pref_up[y + 1]) % MOD  # sum of up[x] for x > y

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD
