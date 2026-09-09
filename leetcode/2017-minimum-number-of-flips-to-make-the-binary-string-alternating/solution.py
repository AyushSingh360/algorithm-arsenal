class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Build two target strings of length 2n: "0101..." and "1010..."
        t1 = []
        t2 = []
        for i in range(2 * n):
            if i % 2 == 0:
                t1.append("0")
                t2.append("1")
            else:
                t1.append("1")
                t2.append("0")
        t1 = "".join(t1)
        t2 = "".join(t2)

        ss = s + s  # to simulate all rotations
        diff1 = diff2 = 0
        ans = n  # upper bound

        left = 0
        for right in range(2 * n):
            # Expand window: compare ss[right] with both patterns
            if ss[right] != t1[right]:
                diff1 += 1
            if ss[right] != t2[right]:
                diff2 += 1

            # When window length > n, shrink from left
            if right - left + 1 > n:
                if ss[left] != t1[left]:
                    diff1 -= 1
                if ss[left] != t2[left]:
                    diff2 -= 1
                left += 1

            # When window length == n, this corresponds to some rotation
            if right - left + 1 == n:
                ans = min(ans, diff1, diff2)

        return ans
