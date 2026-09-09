from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nlen = len(nums)
        self.nums = nums[:]
        # 1‑indexed BIT tree
        self.tree = [0] * (self.nlen + 1)

        # Build the BIT: add each element at its index
        for i in range(self.nlen):
            self._add(i + 1, nums[i])

    def _lowbit(self, x: int) -> int:
        return x & -x

    def _add(self, i: int, delta: int) -> None:
        while i <= self.nlen:
            self.tree[i] += delta
            i += self._lowbit(i)

    def _prefix_sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= self._lowbit(i)
        return s

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum(right + 1) - self._prefix_sum(left)
