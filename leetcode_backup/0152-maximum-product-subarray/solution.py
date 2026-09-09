class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            # Calculate the maximum and minimum product ending at position i
            # We need both max and min because a negative number can turn min into max
            max_product = max(num, max_so_far * num, min_so_far * num)
            min_product = min(num, max_so_far * num, min_so_far * num)

            max_so_far = max_product
            min_so_far = min_product

            result = max(result, max_so_far)

        return result
