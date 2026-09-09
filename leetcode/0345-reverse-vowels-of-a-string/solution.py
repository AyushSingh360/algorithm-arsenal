class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        char_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer until finding a vowel
            while left < right and char_list[left] not in vowels:
                left += 1

            # Move right pointer until finding a vowel
            while left < right and char_list[right] not in vowels:
                right -= 1

            # Swap the vowels
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1

        return "".join(char_list)
