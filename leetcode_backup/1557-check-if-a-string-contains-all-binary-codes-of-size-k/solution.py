class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # If s is too short, impossible to contain all codes
        if len(s) < k:
            return False

        seen = set()
        # Slide window of size k and collect substrings
        for i in range(len(s) - k + 1):
            seen.add(s[i : i + k])

        # There are 2^k possible binary codes of length k
        return len(seen) == (1 << k)
