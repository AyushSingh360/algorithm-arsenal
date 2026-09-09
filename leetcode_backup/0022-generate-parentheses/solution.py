class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtrack(curr, open_cnt, close_cnt):
            # curr: current string, open_cnt: number of '(' used, close_cnt: number of ')' used
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # we can add '(' if we still have some left
            if open_cnt < n:
                backtrack(curr + "(", open_cnt + 1, close_cnt)

            # we can add ')' only if there are more '(' than ')'
            if close_cnt < open_cnt:
                backtrack(curr + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return res
