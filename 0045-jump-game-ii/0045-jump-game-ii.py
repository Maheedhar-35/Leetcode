class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0  
        
        for i in range(n):
            max_jump = nums[i]
            
            for j in range(i + 1, min(i + max_jump + 1, n)):
                if dp[i] + 1 < dp[j]:
                    dp[j] = dp[i] + 1
                    
        return dp[n - 1]