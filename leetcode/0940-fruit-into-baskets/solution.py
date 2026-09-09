class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1

            # Shrink the window if we have more than 2 types
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
