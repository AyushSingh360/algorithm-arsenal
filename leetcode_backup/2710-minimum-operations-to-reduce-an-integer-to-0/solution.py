class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Key insight: count groups of consecutive 1s in binary representation
        # Each isolated 1 needs 1 operation (subtract)
        # Each group of consecutive 1s needs 2 operations (add to next power, then subtract)

        operations = 0

        while n > 0:
            if n & 1:  # If least significant bit is 1
                # Check if there are consecutive 1s
                if n & 2:  # If next bit is also 1
                    # We have consecutive 1s, add to make a single higher bit
                    # This converts 11...1 to 100...0
                    while n & 1:
                        n >>= 1
                    n += 1
                else:
                    # Single 1, just subtract it
                    n -= 1
                operations += 1
            else:
                # Skip zeros
                n >>= 1

        return operations
