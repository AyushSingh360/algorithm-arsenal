class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Max bits needed for right <= 10^6 is < 21, so possible primes in that range:
        prime_counts = {2, 3, 5, 7, 11, 13, 17, 19}

        ans = 0
        for x in range(left, right + 1):
            # Count set bits using builtin
            cnt = bin(x).count("1")
            if cnt in prime_counts:
                ans += 1
        return ans
