from typing import List


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)

        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            step >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        m = len(vals)
        pos = {v: i + 1 for i, v in enumerate(vals)}

        # Fenwick trees for counts and sums
        count = Fenwick(m)
        total = Fenwick(m)

        # Initialize first window
        window_sum = 0

        for i in range(x):
            p = pos[nums[i]]
            count.add(p, 1)
            total.add(p, nums[i])
            window_sum += nums[i]

        costs = []

        # Calculate minimum cost for every window
        for left in range(n - x + 1):

            # Find median (1-indexed lower median)
            mid = count.kth((x + 1) // 2)
            median = vals[mid - 1]

            # Count and sum of elements <= median
            left_count = count.query(mid)
            left_sum = total.query(mid)

            right_count = x - left_count
            right_sum = window_sum - left_sum

            cost = median * left_count - left_sum + right_sum - median * right_count

            costs.append(cost)

            # Slide window
            if left + x < n:
                old = nums[left]
                new = nums[left + x]

                count.add(pos[old], -1)
                total.add(pos[old], -old)

                count.add(pos[new], 1)
                total.add(pos[new], new)

                window_sum += new - old

        # DP: minimum cost to select j non-overlapping windows
        INF = float("inf")

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current element
                curr[i] = curr[i - 1]

                # Take a window ending at i - 1
                if i >= x:
                    curr[i] = min(curr[i], prev[i - x] + costs[i - x])

            prev = curr

        return prev[n]
