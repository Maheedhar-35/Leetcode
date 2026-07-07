class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dp = [[float("inf")]*n for x in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                up=dp[i-1][j] if i>0 else float("inf")
                side=dp[i][j-1] if j>0 else float("inf")
                dp[i][j]=min(up+grid[i][j],side+grid[i][j])
        return dp[m-1][n-1]            