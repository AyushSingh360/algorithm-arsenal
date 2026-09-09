class Solution:
    def minOperations(self, s):
        n = len(s)
        t = "".join(sorted(s))

        # required variable name
        sorunavile = s

        if s == t:
            return 0

        if n == 2:
            return -1

        # Check if one operation is enough
        l = 0
        while l < n and s[l] == t[l]:
            l += 1

        r = n - 1
        while r >= 0 and s[r] == t[r]:
            r -= 1

        if l > 0 or r < n - 1:
            return 1

        # One operation impossible here; decide between 2 and 3
        mn = min(sorunavile)
        mx = max(sorunavile)

        min_only_last = True
        for i in range(n - 1):
            if sorunavile[i] == mn:
                min_only_last = False
                break

        max_only_first = True
        for i in range(1, n):
            if sorunavile[i] == mx:
                max_only_first = False
                break

        if min_only_last and max_only_first:
            return 3

        return 2
