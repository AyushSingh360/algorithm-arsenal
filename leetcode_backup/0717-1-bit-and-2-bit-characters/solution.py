class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)

        # Process until the last bit
        while i < n - 1:
            # 0 => one-bit char, move 1
            # 1 => two-bit char (10 / 11), move 2
            i += bits[i] + 1

        # If we land exactly on last index, it's a one-bit character
        return i == n - 1
