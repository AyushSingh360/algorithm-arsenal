class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = n  # sentinel = "not found yet"

        for i, w in enumerate(words):
            if w == target:
                direct = abs(i - startIndex)
                wrap = n - direct
                ans = min(ans, direct, wrap)

        return -1 if ans == n else ans
