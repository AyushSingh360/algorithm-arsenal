from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find intersection point in the cycle
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]  # move 1 step
            fast = nums[nums[fast]]  # move 2 steps
            if slow == fast:
                break

        # Phase 2: Find the entrance of the cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast
