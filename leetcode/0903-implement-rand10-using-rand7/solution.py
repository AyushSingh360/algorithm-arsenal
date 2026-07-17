# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self) -> int:
        """
        :rtype: int
        """
        while True:
            # Two independent rand7() calls → 7×7 = 49 equally likely outcomes
            row = rand7()  # 1..7
            col = rand7()  # 1..7

            # Map (row, col) to a single number in [1, 49]
            num = (row - 1) * 7 + col  # 1..49 [web:9]

            # Use rejection sampling: only keep 1..40
            if num <= 40:  # 40 = 10 * 4 [web:8][web:9]
                # Uniformly map 1..40 → 1..10
                return 1 + (num - 1) % 10
