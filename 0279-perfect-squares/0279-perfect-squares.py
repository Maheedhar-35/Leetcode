class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[float("inf")]*(n+1)
        dp[0]=0
        Max=int(n**0.5)+1
        arr=[i**2 for i in range(1,Max)]
        for i in range(1,n+1):
            for j in arr:
                if i<j:
                    break
                dp[i]=min(dp[i],dp[i-j]+1)
        return dp[n]            