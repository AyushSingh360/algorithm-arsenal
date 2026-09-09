class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        # Precompute prefix sums of ones
        pref1 = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref1[i + 1] = pref1[i] + (ch == "1")

        # Collect indices of zeros
        zero_pos = []
        for i, ch in enumerate(s):
            if ch == "0":
                zero_pos.append(i)

        # All-ones substrings (0 zeros) are always dominant
        i = 0
        while i < n:
            if s[i] == "1":
                j = i
                while j < n and s[j] == "1":
                    j += 1
                L = j - i
                ans += L * (L + 1) // 2
                i = j
            else:
                i += 1

        # For substrings with k >= 1 zeros, k is at most sqrt(n)
        import math

        K = int(math.isqrt(n)) + 1
        m = len(zero_pos)

        for k in range(1, K + 1):
            if k > m:
                break

            # sliding window over zeros positions: each window has exactly k zeros
            for z_start in range(0, m - k + 1):
                z_end = z_start + k - 1
                left_zero = zero_pos[z_start]
                right_zero = zero_pos[z_end]

                # minimal substring containing these k zeros is [left_zero, right_zero]
                ones_inside = pref1[right_zero + 1] - pref1[left_zero]
                need = k * k - ones_inside
                if need <= 0:
                    need = 0

                # bounds to expand left and right without including another zero
                left_bound = 0 if z_start == 0 else zero_pos[z_start - 1] + 1
                right_bound = n - 1 if z_end == m - 1 else zero_pos[z_end + 1] - 1

                max_left_expand = left_zero - left_bound
                max_right_expand = right_bound - right_zero

                # We want substrings [L, R] with:
                # L in [left_bound, left_zero], R in [right_zero, right_bound]
                # and additional ones (outside [left_zero, right_zero]) >= need.
                # Precompute ones when fully expanded:
                total_ones_full = pref1[right_bound + 1] - pref1[left_bound]
                extra_ones_total = total_ones_full - ones_inside
                if extra_ones_total < need:
                    continue

                # Now binary search minimal total extension length t such that
                # we can gain at least `need` extra ones with some (extend_left, extend_right) where
                # extend_left + extend_right = t, 0 <= extend_left <= max_left_expand, 0 <= extend_right <= max_right_expand.
                # But since ones are not uniformly distributed, we conservatively assume worst-case
                # and treat any extension as potentially adding at most 1 one per step:
                # minimal required total extension length is need.
                # Number of (extend_left, extend_right) with sum >= need is:
                # total_pairs - pairs_with_sum < need

                # total pairs (a,b): 0<=a<=max_left_expand, 0<=b<=max_right_expand
                total_pairs = (max_left_expand + 1) * (max_right_expand + 1)

                # pairs with a+b <= t is triangular; here t = need - 1
                t = need - 1
                if t < 0:
                    # every pair works
                    ans += total_pairs
                    continue

                # compute pairs with a + b <= t
                # a in [0, max_left_expand], for each a, b <= min(max_right_expand, t - a)
                bad = 0
                for a in range(0, max_left_expand + 1):
                    b_max = min(max_right_expand, t - a)
                    if b_max >= 0:
                        bad += b_max + 1

                ans += total_pairs - bad

        return ans
