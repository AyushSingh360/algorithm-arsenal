class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness_sum(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)
            from functools import lru_cache

            # last1, last2 are in [0..9] or 10 as sentinel for "none"
            @lru_cache(maxsize=None)
            def dp(pos: int, tight: int, started: int, last1: int, last2: int):
                # returns (count, waviness_sum)
                if pos == m:
                    # finished number
                    # if not started, we formed just 0 -> waviness 0
                    return (1 if started else 0, 0)

                limit = digits[pos] if tight else 9
                total_count = 0
                total_waviness = 0

                for d in range(0, limit + 1):
                    new_tight = tight and (d == limit)

                    if not started and d == 0:
                        # still leading zeros, number not started
                        cnt, wav = dp(pos + 1, new_tight, 0, 10, 10)
                        total_count += cnt
                        total_waviness += wav
                    else:
                        # we place a real digit
                        new_started = 1

                        added = 0
                        if last2 != 10:
                            # we have at least two previous digits, so last1 can become peak/valley
                            if last1 > last2 and last1 > d:
                                added = 1
                            elif last1 < last2 and last1 < d:
                                added = 1

                        cnt, wav = dp(
                            pos + 1,
                            new_tight,
                            new_started,
                            d,
                            last1 if last1 != 10 else 10,
                        )
                        total_count += cnt
                        total_waviness += wav + added * cnt

                return (total_count, total_waviness)

            return dp(0, 1, 0, 10, 10)[1]

        return waviness_sum(num2) - waviness_sum(num1 - 1)
