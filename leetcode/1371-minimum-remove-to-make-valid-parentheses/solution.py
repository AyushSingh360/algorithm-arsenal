class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass: remove invalid ')'
        tmp = []
        open_count = 0
        for ch in s:
            if ch == ")":
                if open_count == 0:
                    # Skip this unmatched ')'
                    continue
                open_count -= 1
            if ch == "(":
                open_count += 1
            tmp.append(ch)

        # Second pass: remove extra '(' from the end
        res = []
        close_needed = 0
        for ch in reversed(tmp):
            if ch == "(":
                if close_needed == 0:
                    # Skip this unmatched '('
                    continue
                close_needed -= 1
            elif ch == ")":
                close_needed += 1
            res.append(ch)

        return "".join(reversed(res))
