from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        # 32 bits are enough for the given constraints
        for bit in range(32):
            bit_count = 0
            for num in nums:
                if (num >> bit) & 1:
                    bit_count += 1

            if bit_count % 3 != 0:
                # set this bit in result
                res |= 1 << bit

        # handle negative numbers (32-bit signed)
        if res >= (1 << 31):
            res -= 1 << 32
        return res
