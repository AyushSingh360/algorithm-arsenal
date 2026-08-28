class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord("a")] += 1

        # A palindromic permutation is impossible if there are 2+ odd counts.
        odd = [i for i in range(26) if count[i] % 2]
        if len(odd) > 1:
            return ""

        middle = chr(odd[0] + ord("a")) if odd else ""
        half_count = [x // 2 for x in count]
        m = len(s) // 2

        left = []
        equal_prefix = True

        for i in range(m):
            target_char = ord(target[i]) - ord("a")

            # If the prefix is still equal, choose target[i] when available.
            # Otherwise choose the smallest character available.
            start = target_char if equal_prefix else 0

            chosen = -1
            for ch in range(start, 26):
                if half_count[ch] > 0:
                    chosen = ch
                    break

            # No feasible character >= target[i]:
            # backtrack to increase an earlier character.
            if chosen == -1:
                while left:
                    prev = left.pop()
                    half_count[prev] += 1

                    for bigger in range(prev + 1, 26):
                        if half_count[bigger] > 0:
                            half_count[bigger] -= 1
                            left.append(bigger)

                            # Fill the rest with the smallest available chars.
                            for c in range(26):
                                left.extend([c] * half_count[c])

                            left_s = "".join(chr(c + ord("a")) for c in left)
                            ans = left_s + middle + left_s[::-1]
                            return ans

                return ""

            half_count[chosen] -= 1
            left.append(chosen)

            if equal_prefix and chosen > target_char:
                equal_prefix = False

        left_s = "".join(chr(c + ord("a")) for c in left)
        ans = left_s + middle + left_s[::-1]

        # Covers equal-left-half cases, including the middle and mirrored side.
        if ans > target:
            return ans

        # Current palindrome is <= target, so increase the left half minimally.
        for i in range(m - 1, -1, -1):
            current = left[i]
            half_count[current] += 1

            for bigger in range(current + 1, 26):
                if half_count[bigger] > 0:
                    half_count[bigger] -= 1
                    left[i] = bigger

                    for j in range(i + 1, m):
                        for c in range(26):
                            if half_count[c] > 0:
                                left[j] = c
                                half_count[c] -= 1
                                break

                    left_s = "".join(chr(c + ord("a")) for c in left)
                    return left_s + middle + left_s[::-1]

        return ""
