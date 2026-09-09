class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        l = 0
        while l < n and directions[l] == "L":
            l += 1

        r = n - 1
        while r >= 0 and directions[r] == "R":
            r -= 1

        if l > r:
            return 0

        segment = directions[l : r + 1]
        return len(segment) - segment.count("S")
