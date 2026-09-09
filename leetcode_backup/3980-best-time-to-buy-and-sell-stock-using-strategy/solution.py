from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        """
        Return the maximum profit after at most one modification.
        The original profit is the dot product of `strategy` and `prices`.
        A modification selects a sub‑array of length `k` (k is even) and
        forces the first k/2 actions to 0 (hold) and the last k/2 actions to 1 (sell).
        The profit change for a window starting at `s` is therefore:
            delta = sum(prices[s + k/2 : s + k]) -
                    sum(strategy[i] * prices[i] for i in window)
        We take the best (non‑negative) delta and add it to the original profit.
        """
        n = len(prices)
        # Prefix sums for prices and weighted strategy contributions
        price_ps = [0] * (n + 1)
        strat_ps = [0] * (n + 1)
        for i in range(n):
            price_ps[i + 1] = price_ps[i] + prices[i]
            strat_ps[i + 1] = strat_ps[i] + strategy[i] * prices[i]
        # Original profit without any modification
        original = strat_ps[n]
        max_delta = 0
        half = k // 2
        for start in range(0, n - k + 1):
            # Contribution of the whole window in the original strategy
            seg_contrib = strat_ps[start + k] - strat_ps[start]
            # Sum of prices in the last half (which become sells)
            last_half_sum = price_ps[start + k] - price_ps[start + half]
            delta = last_half_sum - seg_contrib
            if delta > max_delta:
                max_delta = delta
        return original + max_delta
