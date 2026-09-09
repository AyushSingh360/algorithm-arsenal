class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        ans = prices[:]  # start with original prices
        stack = []  # will store indices, prices[stack] increasing

        for i in range(n):
            # While current price can serve as discount for previous items
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                ans[idx] = prices[idx] - prices[i]
            stack.append(i)

        return ans
