class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = []

        # Handle negative numbers using two's complement (32-bit)
        num &= 0xFFFFFFFF

        while num:
            # Get the last 4 bits (one hex digit)
            digit = num % 16
            result.append(hex_chars[digit])
            # Remove the last 4 bits
            num //= 16

        # Reverse because we built it from least significant to most
        return "".join(reversed(result))
