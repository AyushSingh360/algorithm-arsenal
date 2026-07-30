class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        ans = 0
        cost = 1  # current push cost for this "layer"

        # Each full layer has 8 letters at the same cost
        for _ in range(n // 8):
            ans += cost * 8
            cost += 1

        # Remaining letters (if any) all have the next cost
        ans += cost * (n % 8)

        return ans
