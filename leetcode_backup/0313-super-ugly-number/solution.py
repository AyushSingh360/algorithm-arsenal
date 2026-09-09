class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        ugly = [1] * n
        idx = [0] * k
        next_vals = primes[:]

        for i in range(1, n):
            nxt = min(next_vals)
            ugly[i] = nxt

            for j in range(k):
                if next_vals[j] == nxt:
                    idx[j] += 1
                    next_vals[j] = ugly[idx[j]] * primes[j]

        return ugly[-1]
