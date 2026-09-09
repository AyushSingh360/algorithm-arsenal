from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        if n == 0:
            return res

        start = nums[0]

        for i in range(1, n):
            # if current number is not consecutive, close the previous range
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

        # close the final range
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")

        return res
