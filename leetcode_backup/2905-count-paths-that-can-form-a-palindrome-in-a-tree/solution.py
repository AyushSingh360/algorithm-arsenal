from collections import defaultdict


class Solution(object):
    def countPalindromePaths(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            g[p].append(i)

        # mask[u]: parity mask from root to u (exclusive of root's "edge char")
        masks = [0] * n

        def dfs_build(u):
            for v in g[u]:
                c = ord(s[v]) - ord("a")
                masks[v] = masks[u] ^ (1 << c)
                dfs_build(v)

        # build masks from root
        dfs_build(0)

        freq = defaultdict(int)
        ans = 0

        # Now count pairs (u, v) with u < v.
        # Using mask[u] ^ mask[v] having at most one bit set.
        for i in range(n):
            m = masks[i]

            # same mask -> all even counts
            ans += freq[m]

            # differ by exactly one bit
            for b in range(26):
                ans += freq[m ^ (1 << b)]

            freq[m] += 1

        return ans
