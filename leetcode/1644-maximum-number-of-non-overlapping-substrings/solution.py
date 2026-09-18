class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        def valid_interval(left: int) -> int:
            right = last[ord(s[left]) - ord('a')]
            i = left

            while i <= right:
                c = ord(s[i]) - ord('a')

                # This character appeared before `left`,
                # so a valid interval cannot start here.
                if first[c] < left:
                    return -1

                right = max(right, last[c])
                i += 1

            return right

        ans = []
        prev_end = -1

        for i in range(n):
            # Only the first occurrence can form the minimal interval
            if i != first[ord(s[i]) - ord('a')]:
                continue

            end = valid_interval(i)
            if end == -1:
                continue

            # A nested valid interval is better: same slot, shorter substring.
            if i > prev_end:
                ans.append(s[i:end + 1])
            else:
                ans[-1] = s[i:end + 1]

            prev_end = end

        return ans
