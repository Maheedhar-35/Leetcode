class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        compressed=[]
        for char in s:
            if not compressed or compressed[-1] != char :
                compressed.append(char)
        s="".join(compressed)
        n=len(s)

        dp=[[0]*n for i in range(n)]
        for i in range(n):
            dp[i][i]=1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                dp[i][j] = dp[i][j-1] + 1
            
                for k in range(i, j):
                    if s[k] == s[j]:
                        turns = dp[i][k] + (dp[k+1][j-1] if k + 1 <= j - 1 else 0)
                        if turns < dp[i][j]:
                            dp[i][j] = turns    
        return dp[0][n-1]