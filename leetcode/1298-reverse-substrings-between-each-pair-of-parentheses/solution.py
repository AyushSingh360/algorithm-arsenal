class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                # Pop until matching '(', collecting characters to reverse
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Remove the '('
                if stack:
                    stack.pop()
                # Push reversed segment back (temp is already in correct order)
                stack.extend(temp)
            else:
                stack.append(c)
        return "".join(stack)
