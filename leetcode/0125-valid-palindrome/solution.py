from typing import List  # not strictly needed for this method, but fine to have


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            # move i forward to next alphanumeric
            while i < j and not s[i].isalnum():
                i += 1
            # move j backward to previous alphanumeric
            while i < j and not s[j].isalnum():
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
