class Solution(object):
    def countOfSubstrings(self, word, k):
        VOWELS = set("aeiou")

        def atMost(K):
            if K < 0:
                return 0
            l = 0
            res = 0
            vowels = 0
            unique_vowels = 0
            last = {}
            for r in range(len(word)):
                c = word[r]
                if c in VOWELS:
                    vowels += 1
                    if last.get(c, -1) < l:
                        unique_vowels += 1
                    last[c] = r

                while (r - l + 1) - vowels > K:
                    d = word[l]
                    if d in VOWELS:
                        vowels -= 1
                        if last.get(d, -1) == l:
                            unique_vowels -= 1
                    l += 1

                if unique_vowels == 5:
                    res += min(last[v] for v in VOWELS) - l + 1
            return res

        return atMost(k) - atMost(k - 1)
