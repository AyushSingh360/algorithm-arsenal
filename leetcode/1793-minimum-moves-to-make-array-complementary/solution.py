from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        ans = n  # upper bound: at most 2 moves per pair => n moves
        # delta[i] = change in required moves when target sum goes from i-1 to i
        delta = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            lo = min(a, b)
            hi = max(a, b)
            pair_sum = a + b

            # For this pair we start with assumption "2 moves for all S"
            # We express improvements (−1 or −2) over ranges as difference-array updates.

            # Range where cost goes from 2 -> 1 (start at lo+1)
            delta[lo + 1] -= 1
            # Exact sum where cost 0 (2 -> 0, so another −1 at pair_sum)
            delta[pair_sum] -= 1
            # From pair_sum+1, we lose that 0-move advantage: cost 0 -> 1 (+1)
            delta[pair_sum + 1] += 1
            # From hi + limit + 1, 1 -> 2 (+1)
            delta[hi + limit + 1] += 1

        moves = n  # start with 2 moves per pair (n/2 * 2) = n
        for s in range(2, 2 * limit + 1):
            moves += delta[s]
            ans = min(ans, moves)

        return ans
