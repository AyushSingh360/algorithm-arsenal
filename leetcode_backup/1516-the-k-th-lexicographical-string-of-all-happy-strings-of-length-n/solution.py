class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = []

        def backtrack(current, prev_char):
            # If we've already found k strings and current is still building,
            # we can stop early
            if len(result) >= k:
                return

            # If current string is of length n, add to result
            if len(current) == n:
                result.append(current)
                return

            # Try adding 'a', 'b', 'c'
            for char in ["a", "b", "c"]:
                # Happy string condition: adjacent characters must be different
                if char != prev_char:
                    backtrack(current + char, char)

        # Start backtracking
        backtrack("", "")

        # Return the kth string (1-indexed), or empty string if not enough
        return result[k - 1] if k <= len(result) else ""
