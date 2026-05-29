class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            # 0 and 1 are perfect squares
            return True

        left, right = 1, num // 2  # sqrt(num) cannot be > num//2 for num > 1

        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
