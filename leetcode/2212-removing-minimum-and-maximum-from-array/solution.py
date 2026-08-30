class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Remove both from front, both from back, or one from each side.
        return min(
            right + 1,
            n - left,
            (left + 1) + (n - right),
        )
