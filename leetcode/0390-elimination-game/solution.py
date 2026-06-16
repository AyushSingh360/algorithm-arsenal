class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1  # first number in current list
        step = 1  # gap between remaining numbers
        remaining = n  # how many numbers still in the list
        left = True  # current direction: True = left->right

        while remaining > 1:
            # If we are moving left, or moving right with odd remaining,
            # the head always gets eliminated, so it shifts forward.
            if left or remaining % 2 == 1:
                head += step

            # After each pass:
            remaining //= 2  # half of the numbers remain
            step *= 2  # gap doubles
            left = not left  # switch direction

        return head
