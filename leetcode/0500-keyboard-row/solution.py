class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []
        for word in words:
            # work in lowercase for case insensitivity
            letters = set(word.lower())
            # check if all letters are contained in any single row
            if letters <= row1 or letters <= row2 or letters <= row3:
                result.append(word)

        return result
