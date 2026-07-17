class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for bit in range(32):
            ones = 0
            for x in nums:
                ones += (x >> bit) & 1
            zeros = n - ones
            ans += ones * zeros

        return ans
