class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for ch in s:
            if "a" <= ch <= "z":
                # Append lowercase letter
                res.append(ch)
            elif ch == "*":
                # Remove last character if it exists
                if res:
                    res.pop()
            elif ch == "#":
                # Duplicate the current result and append
                res = res + res
            elif ch == "%":
                # Reverse the current result
                res.reverse()

        return "".join(res)
