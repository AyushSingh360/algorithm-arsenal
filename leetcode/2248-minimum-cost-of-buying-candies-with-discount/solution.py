class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort in descending order so expensive candies come first
        cost.sort(reverse=True)
        
        total = 0
        # Traverse, skipping every third candy (0-based indexing: indices 0,1 pay; 2 free; 3,4 pay; 5 free; ...)
        for i, c in enumerate(cost):
            if (i + 1) % 3 != 0:  # pay for 1st and 2nd in each group of 3
                total += c
        
        return total
