class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Base case: S1 = "0"
        # Length of Sn is 2^n - 1
        # Middle position of Sn is 2^(n-1)

        def helper(n, k):
            # Base case
            if n == 1:
                return 0  # S1 = "0"

            length = (1 << n) - 1  # 2^n - 1
            mid = 1 << (n - 1)  # 2^(n-1), middle position

            # If k is at the middle, return 1
            if k == mid:
                return 1
            # If k is in the left part, recursively find it in Sn-1
            elif k < mid:
                return helper(n - 1, k)
            # If k is in the right part (inverted and reversed Sn-1)
            else:
                # Position in Sn-1 after reversing
                pos_in_prev = length - k + 1
                # Get the bit from Sn-1 and invert it
                return 1 - helper(n - 1, pos_in_prev)

        return str(helper(n, k))
