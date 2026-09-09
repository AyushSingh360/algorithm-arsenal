from typing import List


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        # Basic matrix validity checks
        for i in range(n):
            if lcp[i][i] != n - i:  # lcp of suffix with itself
                return ""
        for i in range(n):
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""

        # Union-Find for positions that must be equal (lcp[i][j] > 0 ⇒ word[i] == word[j])
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        # From lcp definition: for k in [0, lcp[i][j]) we must have word[i+k] == word[j+k]
        for i in range(n):
            for j in range(n):
                length = lcp[i][j]
                if length == 0:
                    continue
                # If length > n - max(i, j) then impossible
                if i + length > n or j + length > n:
                    return ""
                # Union first characters of the equal prefix
                union(i, j)

        # Assign letters to groups, using as few different letters as possible
        group_char = {}
        next_char_ord = ord("a")
        word = ["?"] * n

        # Sort indices to ensure lexicographically smallest assignment
        for i in range(n):
            root = find(i)
            if root not in group_char:
                if next_char_ord > ord("z"):
                    return ""
                group_char[root] = chr(next_char_ord)
                next_char_ord += 1
            word[i] = group_char[root]

        word_str = "".join(word)

        # Rebuild lcp from word_str to verify consistency
        check = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word_str[i] == word_str[j]:
                    if i == n - 1 or j == n - 1:
                        check[i][j] = 1
                    else:
                        check[i][j] = check[i + 1][j + 1] + 1
                else:
                    check[i][j] = 0
                if check[i][j] != lcp[i][j]:
                    # Early exit on mismatch
                    return ""

        return word_str
