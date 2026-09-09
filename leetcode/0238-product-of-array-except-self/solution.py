class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        # First pass: calculate prefix products
        # answer[i] will contain product of all elements to the left
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Second pass: calculate suffix products and multiply with prefix
        # suffix will contain product of all elements to the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
