from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []

        for x in nums:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)

        return less + equal + greater
