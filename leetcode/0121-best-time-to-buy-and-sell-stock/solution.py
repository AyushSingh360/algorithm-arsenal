class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            # if selling today gives better profit, update
            max_profit = max(max_profit, price - min_price)
            # always keep track of the lowest price so far (best buy)
            min_price = min(min_price, price)

        return max_profit
