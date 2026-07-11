class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*n
        dp[0]=1
        p2=p3=p5=0
        for i in range(1,n):
            n2=dp[p2]*2
            n3=dp[p3]*3
            n5=dp[p5]*5
            ugly=min(n2,n3,n5)
            dp[i]=ugly
            if ugly==n2:
                p2+=1
            if ugly==n3:
                p3+=1
            if ugly==n5:
                p5+=1
        return dp[n-1]                