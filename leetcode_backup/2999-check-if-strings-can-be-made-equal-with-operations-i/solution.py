class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # even indices: 0, 2
        if sorted(s1[0::2]) != sorted(s2[0::2]):
            return False

        # odd indices: 1, 3
        if sorted(s1[1::2]) != sorted(s2[1::2]):
            return False

        return True
