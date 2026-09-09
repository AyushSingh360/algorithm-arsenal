from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        # right[r] = list of left endpoints l for conflicts (l, r) with l < r, 0-based
        right = [[] for _ in range(n)]
        for a, b in conflictingPairs:
            l, r = a - 1, b - 1
            if l > r:
                l, r = r, l
            right[r].append(l)

        result = 0
        # top2[0] = largest left, top2[1] = second largest left, among active blockers
        top2 = [-1, -1]
        # cnt[l] = extra subarrays we gain if we remove the conflict whose left endpoint is l
        cnt = [0] * n

        for r in range(n):
            # insert each left endpoint into top2 in descending order
            for l in right[r]:
                for i in range(2):
                    if l > top2[i]:
                        l, top2[i] = top2[i], l

            # base contribution with current strongest blocker top2[0]
            result += r - top2[0]
            if top2[0] != -1:
                # if we drop the conflict corresponding to top2[0],
                # the second best blocker becomes effective instead
                cnt[top2[0]] += top2[0] - top2[1]

        return result + max(cnt)
