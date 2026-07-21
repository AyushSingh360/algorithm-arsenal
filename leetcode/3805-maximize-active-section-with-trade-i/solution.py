class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        from math import inf

        n = len(s)
        ans = 0
        i = 0
        pre = -inf  # previous zero-run length
        mx = 0  # best sum of two adjacent zero runs

        while i < n:
            j = i + 1
            # find end of current run
            while j < n and s[j] == s[i]:
                j += 1
            cur = j - i  # length of this run

            if s[i] == "1":
                # add all ones directly
                ans += cur
            else:
                # update best adjacent-zero sum
                mx = max(mx, pre + cur)
                pre = cur

            i = j

        # add best gain from one trade
        ans += mx
        return ans
