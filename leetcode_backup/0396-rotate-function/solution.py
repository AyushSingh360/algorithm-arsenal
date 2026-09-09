class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        total = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))  # F(0)
        ans = f

        # Iterate from right to left, using the recurrence:
        # F(k+1) = F(k) + total - n * nums[n-1-k]
        for num in reversed(nums):
            f = f + total - n * num
            ans = max(ans, f)

        return ans
