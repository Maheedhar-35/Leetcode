class Solution(object):
    def climbStairs(self, n, cost):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        if n==1:
            return cost[0]+1
        elif n==2:
            return min(cost[1]+4,cost[0]+1+cost[1]+1)
        dp=[float("inf")]*(n+1)
        dp[0]=0
        dp[1]=cost[0]+1
        dp[2]=min(cost[1]+4,dp[1]+cost[1]+1)
        dp[3]=min(cost[2]+9,dp[1]+cost[2]+4,dp[2]+cost[2]+1)
        for i in range(4,n+1):
            dp[i]=min(dp[i-3]+cost[i-1]+9,dp[i-2]+cost[i-1]+4,dp[i-1]+cost[i-1]+1)
        return dp[n]