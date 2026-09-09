class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []  # function ids
        prevTime = 0

        for log in logs:
            fid_str, typ, time_str = log.split(":")
            fid = int(fid_str)
            t = int(time_str)

            if typ == "start":
                if stack:
                    # add time since prevTime to the function on top
                    res[stack[-1]] += t - prevTime
                stack.append(fid)
                prevTime = t
            else:  # "end"
                # current function ends at t, inclusive
                res[stack.pop()] += t - prevTime + 1
                prevTime = t + 1

        return res
