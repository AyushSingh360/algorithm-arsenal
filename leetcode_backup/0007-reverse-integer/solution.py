class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1
        sign = -1 if x < 0 else 1
        x_abs = abs(x)

        reversed_num = 0
        while x_abs != 0:
            digit = x_abs % 10
            x_abs //= 10
            reversed_num = reversed_num * 10 + digit

        reversed_num *= sign

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        return reversed_num
