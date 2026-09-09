class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # last position of lowercase, first position of uppercase
        lastLower = [-1] * 26
        firstUpper = [len(word)] * 26

        # record positions
        for i, ch in enumerate(word):
            if "a" <= ch <= "z":
                idx = ord(ch) - ord("a")
                lastLower[idx] = i
            else:  # 'A' <= ch <= 'Z'
                idx = ord(ch) - ord("A")
                if firstUpper[idx] == len(word):
                    firstUpper[idx] = i

        # count special letters
        ans = 0
        for i in range(26):
            if (
                lastLower[i] != -1
                and firstUpper[i] != len(word)
                and lastLower[i] < firstUpper[i]
            ):
                ans += 1

        return ans
