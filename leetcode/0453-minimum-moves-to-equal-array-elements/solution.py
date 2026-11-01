class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mn = min(nums)
        return sum(x - mn for x in nums)
