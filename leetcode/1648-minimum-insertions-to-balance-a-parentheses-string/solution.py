class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        opens = 0  # unmatched '('
        need_close = 0  # number of ')' still needed for previous '('

        i = 0
        while i < len(s):
            if s[i] == "(":
                opens += 1
                i += 1
            else:
                # Consume a pair '))' if available
                if i + 1 < len(s) and s[i + 1] == ")":
                    i += 2
                else:
                    ans += 1  # insert one ')' to make '))'
                    i += 1

                if opens:
                    opens -= 1
                else:
                    ans += 1  # need to insert '(' before this '))'

        # Every unmatched '(' needs two closing parentheses
        ans += 2 * opens
        return ans
