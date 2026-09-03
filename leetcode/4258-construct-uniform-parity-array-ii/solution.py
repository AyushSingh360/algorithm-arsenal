class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float("inf")

        for x in nums1:
            if x & 1:
                min_odd = min(min_odd, x)

        # No odd elements => all original values are even.
        if min_odd == float("inf"):
            return True

        # Make all values odd:
        # Every even number needs a smaller odd number.
        can_make_odd = all((x & 1) or x > min_odd for x in nums1)

        # Make all values even:
        # Every odd number must have a smaller odd number available.
        # The minimum odd cannot be converted.
        can_make_even = all(not (x & 1) or x > min_odd for x in nums1)

        return can_make_odd or can_make_even
