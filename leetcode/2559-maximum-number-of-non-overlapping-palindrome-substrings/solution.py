class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        res = 0
        i = 0

        # helper: check if s[l:r+1] is palindrome
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        # greedy: at each position, try to take the shortest palindrome (length k or k+1)
        # so that we can leave more room for later palindromes
        while i + k <= n:
            # try length k
            if is_pal(i, i + k - 1):
                res += 1
                i += k
            # if not, try length k+1 (only if it fits)
            elif i + k < n and is_pal(i, i + k):
                res += 1
                i += k + 1
            else:
                i += 1

        return res
