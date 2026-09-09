from collections import deque
from sortedcontainers import SortedList


class Solution(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        zeros = s.count("0")

        # If no zeros, answer is 0
        if zeros == 0:
            return 0

        # Separate unvisited states by parity
        unvisited_even = SortedList(range(0, n + 1, 2))
        unvisited_odd = SortedList(range(1, n + 1, 2))

        # Determine initial parity and remove initial state
        if zeros % 2 == 0:
            unvisited_even.discard(zeros)
        else:
            unvisited_odd.discard(zeros)

        # BFS
        queue = deque([(zeros, 0)])

        while queue:
            z, ops = queue.popleft()

            if z == 0:
                return ops

            # Calculate range of next states
            min_i = max(0, k - (n - z))
            max_i = min(k, z)

            # All reachable states have the same parity: (z + k) % 2
            new_parity = (z + k) % 2

            if new_parity == 0:
                unvisited = unvisited_even
            else:
                unvisited = unvisited_odd

            # Calculate range of new_z values: z + k - 2*i for i in [min_i, max_i]
            # When i = min_i: new_z = z + k - 2*min_i (maximum)
            # When i = max_i: new_z = z + k - 2*max_i (minimum)
            min_z = z + k - 2 * max_i
            max_z = z + k - 2 * min_i

            # Find indices to delete in the range [min_z, max_z]
            idx_start = unvisited.bisect_left(min_z)
            idx_end = unvisited.bisect_right(max_z)

            # Extract and delete elements in this range
            for j in range(idx_end - 1, idx_start - 1, -1):
                new_z = unvisited[j]
                unvisited.pop(j)
                queue.append((new_z, ops + 1))

        return -1
