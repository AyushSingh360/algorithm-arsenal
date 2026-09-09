class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Use a stack to match brackets
        stack = []

        # Mapping of closing to opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in bracket_map:  # Closing bracket
                # Check if stack is empty or top doesn't match
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:  # Opening bracket
                stack.append(char)

        # Valid if stack is empty (all brackets matched)
        return len(stack) == 0
