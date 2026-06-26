from typing import List
import bisect


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Step 1: build prefix sums after mapping to ±1
        pref = [0] * (n + 1)
        for i in range(n):
            if nums[i] == target:
                pref[i + 1] = pref[i] + 1
            else:
                pref[i + 1] = pref[i] - 1

        # Step 2: coordinate compression of prefix sums
        vals = sorted(set(pref))
        # Fenwick tree size
        m = len(vals)

        def get_id(x: int) -> int:
            # 1-based index for Fenwick
            return bisect.bisect_left(vals, x) + 1

        # Step 3: Fenwick tree implementation
        bit = [0] * (m + 2)

        def bit_add(i: int, delta: int) -> None:
            while i <= m:
                bit[i] += delta
                i += i & -i

        def bit_sum(i: int) -> int:
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        ans = 0
        # Insert pref[0] before processing others
        bit_add(get_id(pref[0]), 1)

        # Step 4: for each current prefix, count previous prefix < current
        for i in range(1, n + 1):
            idx = get_id(pref[i])
            # Number of prefix sums strictly smaller than pref[i]
            cnt_smaller = bit_sum(idx - 1)
            ans += cnt_smaller
            # Insert current prefix
            bit_add(idx, 1)

        return ans
