class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0  # unmatched '(' that need ')'
        close_needed = 0 # unmatched ')' that need '('

        for c in s:
            if c == '(':
                open_needed += 1
            else:  # c == ')'
                if open_needed > 0:
                    # match with a previous '('
                    open_needed -= 1
                else:
                    # no '(' to match, so this ')' is unmatched
                    close_needed += 1

        # open_needed: '(' that never got a ')'
        # close_needed: ')' that never got a '('
        return open_needed + close_needed
