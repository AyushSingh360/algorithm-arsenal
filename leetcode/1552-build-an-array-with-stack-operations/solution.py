class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ops = []
        t_idx = 0
        curr = 1

        while t_idx < len(target) and curr <= n:
            ops.append("Push")
            if curr == target[t_idx]:
                t_idx += 1  # keep it
            else:
                ops.append("Pop")  # discard it
            curr += 1

        return ops
