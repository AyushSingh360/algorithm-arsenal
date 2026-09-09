class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Stack stores (character, count) pairs
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                # Same character as top of stack, increment count
                stack[-1][1] += 1
                # If count reaches k, remove this group
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # Different character, push new entry
                stack.append([char, 1])

        # Build result from stack
        result = []
        for char, count in stack:
            result.append(char * count)

        return "".join(result)
