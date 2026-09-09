class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # lastSeen[c] := last index where c appeared
        last_seen = {"a": -1, "b": -1, "c": -1}
        ans = 0

        for i, ch in enumerate(s):
            last_seen[ch] = i
            # If any char hasn't appeared yet, min will be -1, so we add 0.
            ans += 1 + min(last_seen.values())

        return ans
