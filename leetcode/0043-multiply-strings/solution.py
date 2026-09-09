class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                mul = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j, i + j + 1
                total = mul + result[pos2]

                result[pos2] = total % 10
                result[pos1] += total // 10

        # Skip leading zeros
        i = 0
        while i < len(result) and result[i] == 0:
            i += 1

        return "".join(map(str, result[i:]))
