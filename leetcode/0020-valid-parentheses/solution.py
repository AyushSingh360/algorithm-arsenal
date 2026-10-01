class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in closing:
                if not stack or stack.pop() != closing[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack
