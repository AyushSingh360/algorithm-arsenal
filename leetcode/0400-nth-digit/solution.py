class Solution:
    def findNthDigit(self, n: int) -> int:
        # Initialize digit length and count of numbers with that length
        digit_length = 1  # Start with 1-digit numbers (1-9)
        count = 9  # There are 9 one-digit numbers (1-9)

        # Find the range where the nth digit belongs
        # Keep subtracting total digits until we find the right range
        while digit_length * count < n:
            n -= digit_length * count  # Subtract digits consumed by current range
            digit_length += 1  # Move to next digit length (1->2, 2->3, etc.)
            count *= 10  # Next range has 10x more numbers (9->90->900, etc.)

        # Calculate the actual number containing the nth digit
        # 10^(digit_length-1) gives the starting number of current range
        target_number = 10 ** (digit_length - 1) + (n - 1) // digit_length

        # Find the digit index within the number
        digit_index = (n - 1) % digit_length

        # Convert number to string and extract the digit at calculated index
        return int(str(target_number)[digit_index])
