class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Special case for 0
        if n == 0:
            return 1

        # Find the highest bit position
        temp = n
        mask = 0
        while temp > 0:
            mask = (mask << 1) | 1
            temp >>= 1

        # XOR with mask to flip all bits
        return n ^ mask
