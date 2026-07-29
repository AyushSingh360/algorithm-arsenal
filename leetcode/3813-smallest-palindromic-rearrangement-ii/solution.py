from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        odd = [ch for ch, f in cnt.items() if f % 2]
        if len(odd) > 1:
            return ""
        mid = odd[0] if odd else ""

        half_cnt = [cnt[chr(i + 97)] // 2 for i in range(26)]
        m = sum(half_cnt)

        def nCr_cap(n, r, cap):
            r = min(r, n - r)
            if r < 0:
                return 0
            res = 1
            for i in range(1, r + 1):
                res = res * (n - r + i) // i
                if res >= cap:
                    return cap
            return res

        def count_perms(freq, cap):
            total = sum(freq)
            res = 1
            rem = total
            for f in freq:
                if f:
                    c = nCr_cap(rem, f, cap)
                    res *= c
                    if res >= cap:
                        return cap
                    rem -= f
            return res

        if count_perms(half_cnt, k) < k:
            return ""

        left = []
        for _ in range(m):
            for i in range(26):
                if half_cnt[i] == 0:
                    continue
                half_cnt[i] -= 1
                ways = count_perms(half_cnt, k)
                if ways >= k:
                    left.append(chr(i + 97))
                    break
                k -= ways
                half_cnt[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]
