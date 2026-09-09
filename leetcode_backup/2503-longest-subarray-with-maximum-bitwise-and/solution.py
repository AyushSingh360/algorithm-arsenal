class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        longest = count = 0

        for num in nums:
            if num == max_num:
                count += 1
                longest = max(longest, count)
            else:
                count = 0

        return longest
