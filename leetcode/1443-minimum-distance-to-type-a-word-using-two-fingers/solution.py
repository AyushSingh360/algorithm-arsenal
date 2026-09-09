class Solution:
    def minimumDistance(self, word: str) -> int:
        # Precompute coordinates for each letter
        pos = {}
        for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            pos[ch] = (i // 6, i % 6)

        def dist(a: str, b: str) -> int:
            if a is None or b is None:
                return 0
            (x1, y1), (x2, y2) = pos[a], pos[b]
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(word)
        # dp[j] = minimal cost when one finger is on word[i-1],
        # and the other finger is on letter with index j (0-25) or "none" (-1)
        # We'll compress state: use array of size 27, index 26 = "none"
        INF = 10**9
        dp = [INF] * 27
        # Before typing first char: no second-finger constraint
        # We say second finger is "none" (26) with cost 0
        dp[26] = 0

        for i in range(1, n):
            prev_char = word[i - 1]
            cur_char = word[i]
            prev_idx = ord(prev_char) - ord("A")
            cur_idx = ord(cur_char) - ord("A")

            new_dp = [INF] * 27
            for free_idx in range(27):
                if dp[free_idx] == INF:
                    continue

                # Case 1: move the finger currently on prev_char to cur_char
                # free finger stays where it is (free_idx)
                cost1 = dp[free_idx] + dist(prev_char, cur_char)
                new_dp[free_idx] = min(new_dp[free_idx], cost1)

                # Case 2: move the free finger (at free_idx) to cur_char
                # meaning the free finger was at letter free_idx or none
                free_char = None if free_idx == 26 else chr(free_idx + ord("A"))
                cost2 = dp[free_idx] + dist(free_char, cur_char)
                # now the free finger is at prev_char (index prev_idx)
                new_dp[prev_idx] = min(new_dp[prev_idx], cost2)

            dp = new_dp

        return min(dp)
