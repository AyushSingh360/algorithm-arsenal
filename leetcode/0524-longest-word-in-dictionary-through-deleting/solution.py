class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word: str) -> bool:
            i = 0
            for ch in s:
                if i < len(word) and ch == word[i]:
                    i += 1
            return i == len(word)

        ans = ""
        for word in dictionary:
            if is_subsequence(word):
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word
        return ans
