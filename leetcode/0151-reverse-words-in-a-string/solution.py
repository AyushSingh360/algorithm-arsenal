class Solution:
    def reverseWords(self, s: str) -> str:
        # Split on any amount of whitespace, this automatically
        # removes leading/trailing and collapses multiple spaces
        words = s.split()

        # Reverse the list of words
        words.reverse()  # or words = words[::-1]

        # Join with a single space
        return " ".join(words)
