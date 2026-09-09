class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        ans = 0

        # Precompute first and last occurrence for each letter
        first = [n] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord("a")
            first[idx] = min(first[idx], i)
            last[idx] = max(last[idx], i)

        # For each possible outer character
        for c in range(26):
            if first[c] < last[c]:  # need at least 2 occurrences
                seen = set()
                # Count distinct middle chars between first[c] and last[c]
                for i in range(first[c] + 1, last[c]):
                    seen.add(s[i])
                ans += len(seen)

        return ans
