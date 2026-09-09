class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_recolors = float("inf")
        white_count = 0

        for i in range(len(blocks)):
            if blocks[i] == "W":
                white_count += 1

            if i >= k:
                if blocks[i - k] == "W":
                    white_count -= 1

            if i >= k - 1:
                min_recolors = min(min_recolors, white_count)

        return min_recolors
