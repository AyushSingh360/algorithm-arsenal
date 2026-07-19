class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1  # "1", "12", "122" all have exactly one '1'

        # s will store the magical string as integers 1 and 2
        s = [1, 2, 2]
        head = 2  # position in s that tells us how many times to write next num
        num = 1  # next number to write (alternates between 1 and 2)
        ones = 1  # we already have one '1' in the initial "122"

        # build the string until its length reaches at least n
        while len(s) < n:
            # s[head] is either 1 or 2, meaning we append `num` that many times
            count = s[head]
            for _ in range(count):
                s.append(num)
                # while building, only count '1's if we haven't passed n yet
                if num == 1 and len(s) <= n:
                    ones += 1
            num = 3 - num  # toggle 1 ↔ 2
            head += 1

        return ones
