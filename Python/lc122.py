#find the local min first , then local maximum, and repeat it
#pay attention to edge cases

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
            
        profit = 0
        min_p = prices[0]
        counter = 1
        while counter < len(prices):
            
            while counter<len(prices) and prices[counter]<prices[counter-1]:
                counter += 1
            
            min_p = prices[counter-1]
            
            if counter==len(prices):
                break
            max_p = prices[counter]
            
            counter += 1
            
            while counter<len(prices) and prices[counter]>prices[counter-1]:
                counter += 1
            max_p = prices[counter-1]
            
            profit += max_p - min_p
        return profit
                
