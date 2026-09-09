class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = {}

        for word in words:
            word_map[word] = word_map.get(word, 0) + 1

        result = []

        # Loop over word_len possible start points
        for i in range(word_len):
            left = i
            right = i
            seen = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right : right + word_len]
                right += word_len

                if word in word_map:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    # If word is seen too many times, move left pointer
                    while seen[word] > word_map[word]:
                        left_word = s[left : left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                    # Valid window found
                    if count == word_count:
                        result.append(left)
                else:
                    # Reset window
                    seen.clear()
                    count = 0
                    left = right

        return result
