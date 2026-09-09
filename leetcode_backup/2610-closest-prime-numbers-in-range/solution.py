from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Sieve of Eratosthenes up to right
        is_prime = [True] * (right + 1)
        if right >= 0:
            is_prime[0] = False
        if right >= 1:
            is_prime[1] = False

        p = 2
        while p * p <= right:
            if is_prime[p]:
                for multiple in range(p * p, right + 1, p):
                    is_prime[multiple] = False
            p += 1

        prev = -1
        best_pair = [-1, -1]
        best_diff = float("inf")

        for x in range(max(2, left), right + 1):
            if is_prime[x]:
                if prev != -1 and x - prev < best_diff:
                    best_diff = x - prev
                    best_pair = [prev, x]
                prev = x

        return best_pair
