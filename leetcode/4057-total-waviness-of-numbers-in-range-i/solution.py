class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(x: int) -> int:
            s = str(x)
            n = len(s)
            if n < 3:
                return 0
            cnt = 0
            # check each middle digit i as potential peak/valley
            for i in range(1, n - 1):
                a = int(s[i - 1])
                b = int(s[i])
                c = int(s[i + 1])
                if (b > a and b > c) or (b < a and b < c):
                    cnt += 1
            return cnt

        ans = 0
        for x in range(num1, num2 + 1):
            ans += waviness(x)
        return ans
