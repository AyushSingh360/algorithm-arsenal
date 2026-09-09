from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Store all prefixes of numbers from arr1
        prefixes = set()

        for x in arr1:
            num = x
            while num > 0:
                prefixes.add(num)
                num //= 10  # strip last digit, e.g. 1234 -> 123 -> 12 -> 1

        ans = 0

        # For each number in arr2, check its prefixes from longest to shortest
        for y in arr2:
            num = y
            while num > 0:
                if num in prefixes:
                    # Length of prefix is number of digits
                    ans = max(ans, len(str(num)))
                    break  # no need to check smaller prefixes of this y
                num //= 10

        return ans
