class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = set()
        cur = set()

        for num in arr:
            # New set for current number:
            cur = {num | x for x in cur} | {num}
            result |= cur

        return len(result)
