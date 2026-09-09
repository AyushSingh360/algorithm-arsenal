class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        curr_sum = 0
        ans = float("inf")

        for right in range(n):
            curr_sum += nums[right]

            # shrink window while sum >= target
            while curr_sum >= target:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if ans == float("inf") else ans
