class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = bin(n)[2:]  # binary string without '0b'
        prev = -1
        ans = 0

        for i, ch in enumerate(b):
            if ch == "1":
                if prev != -1:
                    ans = max(ans, i - prev)
                prev = i

        return ans
