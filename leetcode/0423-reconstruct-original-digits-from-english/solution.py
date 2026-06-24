from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        # Count frequency of each character in s
        counter = Counter(s)

        # Array to store count of each digit 0-9
        cnt = [0] * 10

        # Unique letters for certain digits
        cnt[0] = counter['z']  # zero
        cnt[2] = counter['w']  # two
        cnt[4] = counter['u']  # four
        cnt[6] = counter['x']  # six
        cnt[8] = counter['g']  # eight

        # Derived counts for other digits
        cnt[3] = counter['h'] - cnt[8]         # three (h also in eight)
        cnt[5] = counter['f'] - cnt[4]         # five (f also in four)
        cnt[7] = counter['s'] - cnt[6]         # seven (s also in six)
        cnt[1] = counter['o'] - cnt[0] - cnt[2] - cnt[4]  # one
        cnt[9] = counter['i'] - cnt[5] - cnt[6] - cnt[8]  # nine

        # Build result: digits in ascending order
        res = []
        for d in range(10):
            if cnt[d] > 0:
                res.append(str(d) * cnt[d])

        return "".join(res)
