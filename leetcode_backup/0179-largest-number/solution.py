from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all numbers to strings
        nums_str = [str(x) for x in nums]

        # Custom comparator: for two strings a and b,
        # put a before b if a+b is lexicographically larger than b+a
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1  # a should come after b
            else:
                return 0  # a and b are equal in ordering

        # Sort using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))

        # Edge case: if the largest element is "0", the whole number is "0"
        if nums_str[0] == "0":
            return "0"

        # Concatenate to form the largest number
        return "".join(nums_str)
