class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        num=0
        curr=0
        for i in costs:
            if curr+i<=coins and i<coins:
                num+=1
                curr+=i
            else:
                break
        return num                  
