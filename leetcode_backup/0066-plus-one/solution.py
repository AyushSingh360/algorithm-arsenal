class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        carry = 1

        for i in range(n - 1, -1, -1):
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s // 10
            if carry == 0:
                return digits

        if carry:
            return [1] + digits
        return digits
