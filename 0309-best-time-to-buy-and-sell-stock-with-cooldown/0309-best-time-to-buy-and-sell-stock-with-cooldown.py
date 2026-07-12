class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        hold=float("-inf")
        sold=float("-inf")
        reset=0
        for price in prices:
            prevhold=hold
            prevsold=sold
            prevreset=reset

            hold=max(prevhold,prevreset-price)
            sold=prevhold+price
            reset=max(prevsold,prevreset)
        return max(sold,reset)    