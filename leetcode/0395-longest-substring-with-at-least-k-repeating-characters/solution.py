class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        # Count frequency of each character in the entire string
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Find characters that violate the k-repetition requirement
        # Split the string at these characters and recurse
        for char in char_count:
            if char_count[char] < k:
                # Split s at all occurrences of this character
                result = 0
                for substring in s.split(char):
                    result = max(result, self.longestSubstring(substring, k))
                return result

        # All characters in s satisfy the k-repetition requirement
        return len(s)
