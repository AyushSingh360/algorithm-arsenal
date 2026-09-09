class Solution(object):
    def colorTheArray(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nums = [0] * n  # 0 means uncolored
        ans = []
        same = 0  # current count of adjacent equal, non-zero pairs

        for i, c in queries:
            old = nums[i]
            if old == c:
                ans.append(same)
                continue

            # remove old contributions with neighbors
            if old != 0:
                if i - 1 >= 0 and nums[i - 1] == old:
                    same -= 1
                if i + 1 < n and nums[i + 1] == old:
                    same -= 1

            # apply new color
            nums[i] = c

            # add new contributions with neighbors
            if c != 0:
                if i - 1 >= 0 and nums[i - 1] == c:
                    same += 1
                if i + 1 < n and nums[i + 1] == c:
                    same += 1

            ans.append(same)

        return ans
