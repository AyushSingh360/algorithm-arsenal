class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1           # F(0), F(1)
        for _ in range(n):
            a, b = b, a + b   # shift forward in the sequence
        return a
