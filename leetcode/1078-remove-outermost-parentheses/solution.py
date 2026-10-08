class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0

        for ch in s:
            if ch == "(":
                # Skip the opening parenthesis of each primitive
                if depth > 0:
                    result.append(ch)
                depth += 1
            else:
                depth -= 1
                # Skip the closing parenthesis of each primitive
                if depth > 0:
                    result.append(ch)

        return "".join(result)
