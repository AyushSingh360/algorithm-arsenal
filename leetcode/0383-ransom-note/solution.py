class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Frequency array for 'a' to 'z'
        freq = [0] * 26

        # Count characters in magazine
        for ch in magazine:
            freq[ord(ch) - ord('a')] += 1

        # Consume characters for ransomNote
        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            freq[idx] -= 1
            if freq[idx] < 0:
                return False

        return True
