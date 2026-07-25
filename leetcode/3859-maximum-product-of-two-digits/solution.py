class Solution:
    def maxProduct(self, n: int) -> int:
        a = b = 0  # a = largest digit, b = second-largest digit
        while n > 0:
            n, x = divmod(n, 10)  # get last digit x, chop it from n
            if x > a:
                a, b = x, a        # new max; old max becomes second max
            elif x > b:
                b = x              # update second max only
        return a * b
