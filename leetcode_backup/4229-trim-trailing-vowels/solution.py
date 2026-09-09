class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiou")
        i = len(s) - 1

        # Move left while current char is a vowel
        while i >= 0 and s[i] in vowels:
            i -= 1

        # i is now index of last non-vowel, so take prefix up to i
        return s[: i + 1]
