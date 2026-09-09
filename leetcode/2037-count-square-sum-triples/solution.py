class Solution:
    def countTriples(self, n: int) -> int:
        # Precompute all squares up to n and store in a set
        squares = {i * i for i in range(1, n + 1)}

        ans = 0
        # Try all pairs (a, b)
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a * a + b * b in squares:
                    ans += 1

        return ans
