from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # monotonic decreasing stack for potential nums[j]
        third = float("-inf")  # best candidate for nums[k] (the "2" in 132)

        # iterate from right to left
        for num in reversed(nums):
            # if we find num < third, we've found nums[i] < nums[k] < nums[j]
            if num < third:
                return True

            # maintain decreasing stack; popped values become candidates for nums[k]
            while stack and num > stack[-1]:
                third = stack.pop()

            # current num is a new candidate for nums[j]
            stack.append(num)

        return False
