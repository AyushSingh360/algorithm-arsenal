from collections import defaultdict
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)

        # Group indices by value
        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = [0] * n

        for indices in pos.values():
            m = len(indices)
            if m == 1:
                ans[indices[0]] = 0
                continue

            # Initial sum for the first index:
            # sum_{k=1..m-1} (indices[k] - indices[0])
            total_sum = sum(indices)
            curr = total_sum - indices[0] * m

            # Fill for each index in this group
            for i, idx in enumerate(indices):
                if i > 0:
                    diff = indices[i] - indices[i - 1]
                    # Left side gets closer, right side gets farther
                    curr += i * diff - (m - i) * diff
                ans[idx] = curr

        return ans
