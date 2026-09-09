from typing import *


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        # sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        # use abs values
        num = abs(numerator)
        den = abs(denominator)

        # integer part
        integer_part = num // den
        res.append(str(integer_part))

        remainder = num % den
        if remainder == 0:
            return "".join(res)

        # decimal point
        res.append(".")

        # map: remainder -> index in res where its quotient digit is placed
        rem_index = {}

        while remainder != 0:
            if remainder in rem_index:
                # insert '(' at the first occurrence index
                idx = rem_index[remainder]
                res.insert(idx, "(")
                res.append(")")
                break

            rem_index[remainder] = len(res)

            remainder *= 10
            digit = remainder // den
            res.append(str(digit))
            remainder %= den

        return "".join(res)
