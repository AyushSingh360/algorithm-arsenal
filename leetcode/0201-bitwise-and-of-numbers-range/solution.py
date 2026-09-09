class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Find common prefix
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        # Shift prefix back to original position
        return left << shift
