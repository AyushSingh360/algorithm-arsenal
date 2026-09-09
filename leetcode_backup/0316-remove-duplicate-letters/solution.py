class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = {c: i for i, c in enumerate(s)}  # last index of each char
        stack = []
        in_stack = set()

        for i, c in enumerate(s):
            if c in in_stack:
                continue

            # maintain increasing (lexicographically) stack
            while stack and c < stack[-1] and last[stack[-1]] > i:
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(c)
            in_stack.add(c)

        return "".join(stack)
