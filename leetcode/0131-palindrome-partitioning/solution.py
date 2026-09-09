class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def is_pal(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start: int) -> None:
            # If we've used all characters, current partition is a valid answer
            if start == len(s):
                res.append(part.copy())
                return

            # Try all possible end positions for current substring
            for end in range(start, len(s)):
                if is_pal(start, end):
                    # Choose
                    part.append(s[start : end + 1])
                    # Explore
                    backtrack(end + 1)
                    # Un-choose
                    part.pop()

        backtrack(0)
        return res
