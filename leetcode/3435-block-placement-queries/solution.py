from typing import List
import bisect


class SegTree:
    def __init__(self, positions):
        self.positions = positions
        n = len(positions)
        size = 1
        while size < n:
            size <<= 1
        self.size = size
        self.max_gap = [0] * (2 * size)
        self.left = [None] * (2 * size)
        self.right = [None] * (2 * size)

    def _pull(self, i):
        lc = i * 2
        rc = i * 2 + 1
        self.max_gap[i] = max(self.max_gap[lc], self.max_gap[rc])
        self.left[i] = self.left[lc] if self.left[lc] is not None else self.left[rc]
        self.right[i] = self.right[rc] if self.right[rc] is not None else self.right[lc]
        if self.right[lc] is not None and self.left[rc] is not None:
            cross = self.left[rc] - self.right[lc]
            if cross > self.max_gap[i]:
                self.max_gap[i] = cross

    def _merge(self, a_max, a_left, a_right, b_max, b_left, b_right):
        if a_left is None:
            return b_max, b_left, b_right
        if b_left is None:
            return a_max, a_left, a_right
        new_max = max(a_max, b_max)
        if a_right is not None and b_left is not None:
            cross = b_left - a_right
            if cross > new_max:
                new_max = cross
        return new_max, a_left, b_right

    def add(self, pos):
        idx = bisect.bisect_left(self.positions, pos)
        i = idx + self.size
        self.left[i] = pos
        self.right[i] = pos
        self.max_gap[i] = 0
        i //= 2
        while i:
            self._pull(i)
            i //= 2

    def query(self, r_idx):
        if r_idx < 0:
            return 0, None, None
        l = self.size
        r = r_idx + self.size + 1
        l_max, l_left, l_right = 0, None, None
        r_max, r_left, r_right = 0, None, None
        while l < r:
            if l & 1:
                l_max, l_left, l_right = self._merge(
                    l_max, l_left, l_right,
                    self.max_gap[l], self.left[l], self.right[l]
                )
                l += 1
            if r & 1:
                r -= 1
                r_max, r_left, r_right = self._merge(
                    self.max_gap[r], self.left[r], self.right[r],
                    r_max, r_left, r_right
                )
            l //= 2
            r //= 2
        return self._merge(l_max, l_left, l_right, r_max, r_left, r_right)


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        pos_set = {0}
        for q in queries:
            if q[0] == 1:
                pos_set.add(q[1])
            else:
                pos_set.add(q[1])
        positions = sorted(pos_set)

        seg = SegTree(positions)
        seg.add(0)

        results = []
        for q in queries:
            if q[0] == 1:
                _, x = q
                seg.add(x)
            else:
                _, x, sz = q
                r_idx = bisect.bisect_right(positions, x) - 1
                mg, _, ro = seg.query(r_idx)
                candidate = mg
                if ro is not None:
                    candidate = max(candidate, x - ro)
                else:
                    candidate = x
                results.append(candidate >= sz)

        return results
