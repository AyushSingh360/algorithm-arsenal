# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2  # avoid overflow style, though in Python it's safe
            res = guess(mid)

            if res == 0:
                return mid
            elif res < 0:      # mid is higher than pick
                right = mid - 1
            else:              # mid is lower than pick
                left = mid + 1

        # In this problem we are guaranteed to find the number,
        # so this return is never actually reached.
        return -1
