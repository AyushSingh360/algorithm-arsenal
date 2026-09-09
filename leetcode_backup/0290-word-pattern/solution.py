class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # If counts differ, impossible to match
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for ch, w in zip(pattern, words):
            # If we've seen the char before, its mapped word must match
            if ch in char_to_word:
                if char_to_word[ch] != w:
                    return False
            else:
                char_to_word[ch] = w

            # If we've seen the word before, its mapped char must match
            if w in word_to_char:
                if word_to_char[w] != ch:
                    return False
            else:
                word_to_char[w] = ch

        return True
