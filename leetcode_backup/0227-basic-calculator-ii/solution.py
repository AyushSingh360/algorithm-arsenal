class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"  # previous operator

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)

            # if c is an operator or we're at the end, process the previous sign
            if c in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    prev = stack.pop()
                    # truncate toward zero
                    stack.append(int(prev / num))

                sign = c
                num = 0

        return sum(stack)
