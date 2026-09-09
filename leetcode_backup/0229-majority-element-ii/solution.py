from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # 1st pass: find up to two candidates
        cand1 = cand2 = None
        count1 = count2 = 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # 2nd pass: verify actual counts
        res = []
        n = len(nums)
        threshold = n // 3

        c1 = c2 = 0
        for num in nums:
            if num == cand1:
                c1 += 1
            elif num == cand2:
                c2 += 1

        if c1 > threshold:
            res.append(cand1)
        if c2 > threshold:
            res.append(cand2)

        return res
