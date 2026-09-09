class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        ans = -1
        best = 10**9  # larger than any possible capacity

        for i, c in enumerate(capacity):
            if c >= itemSize and c < best:
                best = c
                ans = i

        return ans
