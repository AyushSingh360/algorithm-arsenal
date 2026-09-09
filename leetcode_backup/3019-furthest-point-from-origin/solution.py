class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = moves.count("L")
        right = moves.count("R")
        wild = moves.count("_")

        # Net displacement from fixed moves is |L - R|,
        # then every '_' can be used to extend this distance by 1.
        return abs(left - right) + wild
