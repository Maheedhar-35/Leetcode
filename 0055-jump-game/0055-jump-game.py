class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [False] * n
        dp[0] = True  
        
        for i in range(1,n):
            if dp[n-1]:
                return True
            j=i-1    
            while j>=0:
                if dp[j]:
                    if j+nums[j]>=i:
                        dp[i]=True
                        break
                j=j-1    

        return dp[n - 1]