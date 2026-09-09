from collections import deque


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        max_val = max(nums)

        # 1. Sieve of Eratosthenes to find the Smallest Prime Factor (SPF)
        # This allows us to factorize any number in O(log(val)) time.
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Helper function to get unique prime factors using SPF
        def get_prime_factors(num):
            factors = set()
            while num > 1:
                p = spf[num]
                factors.add(p)
                while num % p == 0:
                    num //= p
            return factors

        # 2. Map every prime factor to the indices where nums[j] % p == 0
        prime_to_indices = {}
        # Pre-calculating prime factors for each index
        index_to_primes = []
        for idx, val in enumerate(nums):
            primes = get_prime_factors(val)
            index_to_primes.append(primes)
            for p in primes:
                if p not in prime_to_indices:
                    prime_to_indices[p] = []
                prime_to_indices[p].append(idx)

        # 3. BFS for Shortest Path
        queue = deque([(0, 0)])  # (current_index, jumps)
        visited_indices = {0}
        visited_primes = set()

        while queue:
            curr_idx, dist = queue.popleft()

            # Goal reached
            if curr_idx == n - 1:
                return dist

            # Strategy A: Adjacent Steps
            for neighbor in [curr_idx - 1, curr_idx + 1]:
                if 0 <= neighbor < n and neighbor not in visited_indices:
                    visited_indices.add(neighbor)
                    queue.append((neighbor, dist + 1))

            # Strategy B: Prime Teleportation
            # We only check teleportation if the current number itself IS prime (p)
            # and jump to any index j where nums[j] % p == 0.
            val = nums[curr_idx]

            # Check if nums[curr_idx] is a prime number
            if val > 1 and spf[val] == val:
                p = val
                if p not in visited_primes:
                    visited_primes.add(p)
                    if p in prime_to_indices:
                        for next_idx in prime_to_indices[p]:
                            if next_idx not in visited_indices:
                                visited_indices.add(next_idx)
                                queue.append((next_idx, dist + 1))

        return -1
