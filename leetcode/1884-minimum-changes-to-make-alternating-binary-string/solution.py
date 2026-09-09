class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            expected = "0" if i % 2 == 0 else "1"
            if s[i] != expected:
                count += 1
        return min(count, len(s) - count)
