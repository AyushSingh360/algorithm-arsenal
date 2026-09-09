class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        L = n + m - 1

        word = ["?"] * L
        fixed = [False] * L

        # 1) Force every T-window to equal str2.
        for i, ch in enumerate(str1):
            if ch == "T":
                for j in range(m):
                    pos = i + j
                    if word[pos] != "?" and word[pos] != str2[j]:
                        return ""
                    word[pos] = str2[j]
                    fixed[pos] = True

        # 2) Fill remaining positions with 'a' for lexicographically smallest start.
        for i in range(L):
            if word[i] == "?":
                word[i] = "a"

        # 3) For every F-window that accidentally equals str2,
        #    break it by changing the rightmost modifiable position to 'b'
        #    (or 'a' if str2 char there isn't 'a').
        for i, ch in enumerate(str1):
            if ch == "F":
                matches = True
                for j in range(m):
                    if word[i + j] != str2[j]:
                        matches = False
                        break
                if not matches:
                    continue

                changed = False
                for j in range(m - 1, -1, -1):
                    pos = i + j
                    if not fixed[pos]:
                        word[pos] = "b" if str2[j] == "a" else "a"
                        changed = True
                        break

                if not changed:
                    return ""

        # 4) Final verification.
        ans = "".join(word)
        for i, ch in enumerate(str1):
            sub = ans[i : i + m]
            if ch == "T" and sub != str2:
                return ""
            if ch == "F" and sub == str2:
                return ""
        return ans
