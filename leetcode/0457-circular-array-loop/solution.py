from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        def next_index(i: int) -> int:
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, i
            direction = nums[i] > 0  # True for positive (forward), False for negative (backward)

            while True:
                # move slow one step
                nxt_slow = next_index(slow)
                # move fast one step, then another (two steps total)
                nxt_fast = next_index(fast)
                nxt_fast2 = next_index(nxt_fast)

                # Check direction consistency for next positions
                if (nums[nxt_slow] > 0) != direction or (nums[nxt_fast] > 0) != direction or (nums[nxt_fast2] > 0) != direction:
                    break

                slow = nxt_slow
                fast = nxt_fast2

                # if they meet, check cycle length > 1
                if slow == fast:
                    if slow == next_index(slow):  # single-element loop
                        break
                    return True

            # mark all nodes in this traversal as 0 to skip later
            j = i
            sign = nums[i] > 0
            while nums[j] != 0 and (nums[j] > 0) == sign:
                nxt = next_index(j)
                nums[j] = 0
                j = nxt

        return False
