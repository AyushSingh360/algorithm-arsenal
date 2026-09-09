class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = {}

        for row, seat in reservedSeats:
            # Seats 1 and 10 never affect a valid four-seat block.
            if 2 <= seat <= 9:
                reserved[row] = reserved.get(row, 0) | (1 << seat)

        # Every completely unreserved row fits two families: [2..5] and [6..9].
        ans = 2 * n

        left = sum(1 << seat for seat in range(2, 6))  # 2,3,4,5
        middle = sum(1 << seat for seat in range(4, 8))  # 4,5,6,7
        right = sum(1 << seat for seat in range(6, 10))  # 6,7,8,9

        for mask in reserved.values():
            ans -= 2

            if mask & left == 0 and mask & right == 0:
                ans += 2
            elif mask & left == 0 or mask & middle == 0 or mask & right == 0:
                ans += 1

        return ans
