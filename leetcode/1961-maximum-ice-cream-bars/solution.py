from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if not costs:
            return 0
        
        max_cost = max(costs)
        
        # freq[c] = how many bars cost 'c'
        freq = [0] * (max_cost + 1)
        for c in costs:
            freq[c] += 1
        
        bars = 0
        
        # Go from cheapest to most expensive
        for cost in range(1, max_cost + 1):
            if freq[cost] == 0:
                continue
            if coins < cost:
                break  # Can't afford even one bar of this cost
            
            # Max number of bars we can buy at this cost
            can_buy = min(freq[cost], coins // cost)
            bars += can_buy
            coins -= can_buy * cost
            
            if coins == 0:
                break
        
        return bars
