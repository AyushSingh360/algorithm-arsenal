class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        ans = []
        n = len(s)

        # Build the longest prefix equal to target.
        i = 0
        while i < n:
            x = ord(target[i]) - ord('a')

            if freq[x] == 0:
                break

            freq[x] -= 1
            ans.append(target[i])
            i += 1

        # Try to make position i larger first.
        # If impossible, backtrack and try earlier positions.
        while i >= 0:
            if i < n:
                needed = ord(target[i]) - ord('a')

                for c in range(needed + 1, 26):
                    if freq[c] > 0:
                        freq[c] -= 1
                        ans.append(chr(ord('a') + c))

                        # Smallest suffix after becoming greater.
                        for k in range(26):
                            ans.extend(chr(ord('a') + k) * freq[k])

                        return ''.join(ans)

            # Cannot increase at i: restore the previous matched character.
            if i == 0:
                break

            i -= 1
            ch = ans.pop()
            freq[ord(ch) - ord('a')] += 1

        return ""
