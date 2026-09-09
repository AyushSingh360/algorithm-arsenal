# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        first_bad = n  # or any sentinel within [1, n]

        while left <= right:
            mid = left + (right - left) // 2  # avoids overflow in other languages
            if isBadVersion(mid):
                first_bad = mid  # mid is bad, so record it
                right = mid - 1  # and search earlier versions
            else:
                left = mid + 1  # mid is good, so search later versions

        return first_bad
