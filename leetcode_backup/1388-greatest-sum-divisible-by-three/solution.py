from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        r = total % 3
        if r == 0:
            return total

        rem1 = []
        rem2 = []
        for x in nums:
            if x % 3 == 1:
                rem1.append(x)
            elif x % 3 == 2:
                rem2.append(x)

        rem1.sort()
        rem2.sort()

        INF = 10**18
        remove = INF

        if r == 1:
            if rem1:
                remove = min(remove, rem1[0])
            if len(rem2) >= 2:
                remove = min(remove, rem2[0] + rem2[1])
        else:  # r == 2
            if rem2:
                remove = min(remove, rem2[0])
            if len(rem1) >= 2:
                remove = min(remove, rem1[0] + rem1[1])

        if remove == INF:
            return 0
        return total - remove
