class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # If both strings are exactly the same, all subsequences are common
        if a == b:
            return -1
        # Otherwise, the longer string itself is an uncommon subsequence
        return max(len(a), len(b))
