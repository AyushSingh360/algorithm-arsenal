class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Use a stack to build the smallest possible number
        stack = []

        # Calculate how many digits we need to keep in the final result
        remaining_digits = len(num) - k

        # Iterate through each digit in the input number
        for digit in num:
            # While we still have removals left (k > 0)
            # and the stack is not empty
            # and the top of stack is greater than current digit
            # Remove the larger digit from stack to maintain smallest number
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            # Add current digit to the stack
            stack.append(digit)

        # Take only the required number of digits from the stack
        # Remove leading zeros and return '0' if the result is empty
        result = "".join(stack[:remaining_digits]).lstrip("0")
        return result if result else "0"
