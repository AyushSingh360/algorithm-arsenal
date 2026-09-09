class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Lengths must be equal to be rotations of each other
        if len(s) != len(goal):
            return False
        # If goal is a rotation of s, it must appear in s + s
        return goal in (s + s)
