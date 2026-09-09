class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ""

        subs = []
        bal = 0
        start = 0

        # decompose into top-level special substrings
        for i, ch in enumerate(s):
            bal += 1 if ch == "1" else -1
            if bal == 0:
                # inner part is s[start+1:i]
                inner = self.makeLargestSpecial(s[start + 1 : i])
                subs.append("1" + inner + "0")
                start = i + 1

        # sort in reverse lexicographic order and concatenate
        subs.sort(reverse=True)
        return "".join(subs)
