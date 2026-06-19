class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0          # starting altitude
        curr = 0             # current altitude

        for g in gain:
            curr += g        # update current altitude
            highest = max(highest, curr)

        return highest
