class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # Mark seen numbers by negating the value at their index (value-1)
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Indices with positive values correspond to missing numbers
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)

        return res
