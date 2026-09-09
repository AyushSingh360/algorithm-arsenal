class NumArray:

    def __init__(self, nums: List[int]):
        # prefix[i] will store sum of nums[0 .. i-1]
        self.prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + x

    def sumRange(self, left: int, right: int) -> int:
        # sum of nums[left .. right] = prefix[right + 1] - prefix[left]
        return self.prefix[right + 1] - self.prefix[left]
