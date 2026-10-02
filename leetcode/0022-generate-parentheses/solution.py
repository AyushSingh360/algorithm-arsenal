class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(s: str, open_count: int, close_count: int) -> None:
            # If the current string is complete
            if len(s) == 2 * n:
                res.append(s)
                return

            # We can add an open bracket if we haven't used all n
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            # We can add a close bracket if it won't exceed open_count
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res
