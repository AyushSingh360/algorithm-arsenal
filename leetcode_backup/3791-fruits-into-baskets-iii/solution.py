class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(baskets)
        size = 1
        while size < n:
            size <<= 1

        seg = [0] * (2 * size)

        for i in range(n):
            seg[size + i] = baskets[i]
        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[i << 1], seg[i << 1 | 1])

        def first_ge(value):
            if seg[1] < value:
                return -1
            idx = 1
            l, r = 0, size - 1
            while l != r:
                mid = (l + r) // 2
                left = idx << 1
                if seg[left] >= value:
                    idx = left
                    r = mid
                else:
                    idx = left | 1
                    l = mid + 1
            return l if l < n and seg[idx] >= value else -1

        def update(pos, val):
            i = size + pos
            seg[i] = val
            i >>= 1
            while i:
                seg[i] = max(seg[i << 1], seg[i << 1 | 1])
                i >>= 1

        unplaced = 0
        for f in fruits:
            pos = first_ge(f)
            if pos == -1:
                unplaced += 1
            else:
                update(pos, 0)

        return unplaced
