from typing import List

class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)
        size = 1
        while size < n:
            size <<= 1

        # Node format:
        # [left_char, right_char, prefix_length, suffix_length, best_length, total_length]
        tree = [[None, None, 0, 0, 0, 0] for _ in range(2 * size)]

        def merge(left, right):
            if left[5] == 0:
                return right
            if right[5] == 0:
                return left

            lc, rc = left[0], right[1]
            total = left[5] + right[5]

            prefix = left[2]
            if left[2] == left[5] and left[1] == right[0]:
                prefix = left[5] + right[2]

            suffix = right[3]
            if right[3] == right[5] and left[1] == right[0]:
                suffix = right[5] + left[3]

            best = max(left[4], right[4])
            if left[1] == right[0]:
                best = max(best, left[3] + right[2])

            return [lc, rc, prefix, suffix, best, total]

        # Build leaves
        for i, ch in enumerate(s):
            tree[size + i] = [ch, ch, 1, 1, 1, 1]

        # Build internal nodes
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(pos, ch):
            node = size + pos
            tree[node] = [ch, ch, 1, 1, 1, 1]

            node //= 2
            while node:
                tree[node] = merge(tree[2 * node], tree[2 * node + 1])
                node //= 2

        ans = []

        for ch, index in zip(queryCharacters, queryIndices):
            update(index, ch)
            ans.append(tree[1][4])

        return ans
