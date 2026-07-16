class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        res = 0
        j = 0
        n = len(heaters)

        for house in houses:
            while j + 1 < n and abs(heaters[j + 1] - house) <= abs(heaters[j] - house):
                j += 1
            res = max(res, abs(heaters[j] - house))

        return res
