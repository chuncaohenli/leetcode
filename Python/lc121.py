# scan the array for once, and record the minimum price and maximum profit for each element

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        
        min_price = prices[0]
        profit = 0
        
        for p in prices:
            min_price = min(p,min_price)
            profit = max(profit,p-min_price)
        return profit
