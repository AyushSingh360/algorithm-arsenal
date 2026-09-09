from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        # next_idx[i] = next occurrence index of nums[i] (or -1 if none)
        next_idx = [-1] * n
        # last_pos[val] = last index where value 'val' was seen while scanning from right
        # values are in [1, n], so we need size n + 1
        last_pos = [-1] * (n + 1)

        # Build next pointers from right to left
        for i in range(n - 1, -1, -1):
            v = nums[i]
            next_idx[i] = last_pos[v]
            last_pos[v] = i

        ans = float("inf")

        # For each index, try to form a triple using consecutive occurrences
        for i in range(n):
            second = next_idx[i]
            if second == -1:
                continue
            third = next_idx[second]
            if third == -1:
                continue
            # distance = 2 * (third - i)
            ans = min(ans, 2 * (third - i))

        return -1 if ans == float("inf") else ans
