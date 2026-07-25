class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        total = 1
        i = 2

        while i * i <= num:
            if num % i == 0:
                total += i
                other = num // i
                if other != i:
                    total += other
            i += 1

        return total == num
