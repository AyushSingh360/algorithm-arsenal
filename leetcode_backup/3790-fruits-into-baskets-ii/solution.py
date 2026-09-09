class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        used = [False] * n  # Track whether a basket is used
        unplaced = 0

        for i in range(n):
            placed = False
            for j in range(n):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced


# Example usage
sol = Solution()
print(sol.numOfUnplacedFruits([4, 2, 2, 2], [1, 4, 1, 2]))  # Output: 1
