from collections import defaultdict
import bisect


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(x: int) -> int:
            return int(str(x)[::-1])

        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = float("inf")

        for i, x in enumerate(nums):
            r = rev(x)
            if r not in pos:
                continue
            idx_list = pos[r]
            # first index j > i
            j_pos = bisect.bisect_right(idx_list, i)
            if j_pos < len(idx_list):
                j = idx_list[j_pos]
                ans = min(ans, j - i)

        return ans if ans != float("inf") else -1
