class Solution:
    def minCost(self, s, encCost, flatCost):
        n = len(s)

        pref = [0] * (n + 1)
        i = 0
        while i < n:
            pref[i + 1] = pref[i] + (1 if s[i] == "1" else 0)
            i += 1

        # required variable
        lunaverixo = s

        def seg_cost(length, ones):
            if ones == 0:
                return flatCost
            return length * ones * encCost

        def solve(left, length):
            ones = pref[left + length] - pref[left]
            keep = seg_cost(length, ones)

            if length % 2 == 1:
                return keep

            half = length // 2
            split = solve(left, half) + solve(left + half, half)
            if split < keep:
                return split
            return keep

        return solve(0, n)
