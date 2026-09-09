class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = float("inf")
        for i, val in enumerate(nums):
            if val == target:
                ans = min(ans, abs(i - start))
        return ans
