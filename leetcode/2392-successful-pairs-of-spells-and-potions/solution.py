class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            min_potion = (success + spell - 1) // spell

            left, right = 0, m
            while left < right:
                mid = (left + right) // 2
                if potions[mid] >= min_potion:
                    right = mid
                else:
                    left = mid + 1

            result.append(m - left)

        return result
