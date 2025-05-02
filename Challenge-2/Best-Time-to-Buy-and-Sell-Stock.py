class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        minimum=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>minimum:
                max_profit=max(max_profit,prices[i]-minimum)
            else:
                minimum=prices[i]
        return max_profit


