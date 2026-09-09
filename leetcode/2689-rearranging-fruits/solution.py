from collections import Counter


class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        count1 = Counter(basket1)
        count2 = Counter(basket2)

        total = count1 + count2

        # Step 1: Check feasibility
        for fruit in total:
            if total[fruit] % 2 != 0:
                return -1

        # Step 2: Get surplus from both baskets
        surplus = []

        for fruit in total:
            diff = count1[fruit] - (total[fruit] // 2)
            if diff > 0:
                surplus.extend([fruit] * diff)

        for fruit in total:
            diff = count2[fruit] - (total[fruit] // 2)
            if diff > 0:
                surplus.extend([fruit] * diff)

        if not surplus:
            return 0

        surplus.sort()
        min_fruit = min(total)

        # Step 3: Pair half of the surplus (we consider only half swaps)
        swaps = len(surplus) // 2
        cost = 0
        for i in range(swaps):
            cost += min(surplus[i], 2 * min_fruit)

        return cost
