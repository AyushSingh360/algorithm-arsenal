class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                if current > max_count:
                    max_count = current
            else:
                current = 0

        return max_count
