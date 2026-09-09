from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cnt_secret = Counter()
        cnt_guess = Counter()

        # First pass: count bulls and build freq maps for non-bulls
        for s_ch, g_ch in zip(secret, guess):
            if s_ch == g_ch:
                bulls += 1
            else:
                cnt_secret[s_ch] += 1
                cnt_guess[g_ch] += 1

        # Cows are the sum of minimum matches for each digit
        cows = 0
        for digit in cnt_secret:
            cows += min(cnt_secret[digit], cnt_guess.get(digit, 0))

        return f"{bulls}A{cows}B"
