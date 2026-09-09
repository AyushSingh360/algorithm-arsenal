class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None (modifies nums in-place)
        """
        n = len(nums)
        i = n - 2

        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the next larger element to the right of i
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the subarray to the right of i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
