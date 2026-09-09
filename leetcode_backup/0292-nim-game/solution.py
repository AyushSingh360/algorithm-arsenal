class Solution:
    def canWinNim(self, n: int) -> bool:
        # If n is a multiple of 4, the opponent can always mirror your moves
        # to keep you at multiples of 4 and take the last stone.
        # Otherwise, you can move first to a multiple of 4 and then mirror them.
        return n % 4 != 0
