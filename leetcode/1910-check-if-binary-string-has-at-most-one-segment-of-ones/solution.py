class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Idea: once we see "01", there must not be any '1' after it
        # So if the pattern "01" appears and later we see '1', return False.
        seen_zero_after_one = False
        for ch in s:
            if ch == "0":
                seen_zero_after_one = True
            else:  # ch == '1'
                if seen_zero_after_one:
                    return False
        return True
