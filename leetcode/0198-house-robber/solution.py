class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # prev2 = best we could do up to house i-2
        # prev1 = best we could do up to house i-1
        prev2 = 0
        prev1 = 0

        for money in nums:
            # either rob this house (prev2 + money) or skip it (prev1)
            curr = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = curr

        return prev1
