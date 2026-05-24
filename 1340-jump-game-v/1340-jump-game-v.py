class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        memo = [-1] * n
        
        def dfs(i):
            if memo[i] != -1:
                return memo[i]
            
            max_steps = 1
            
            for x in range(1, d + 1):
                j = i + x
                if j >= n or arr[j] >= arr[i]:
                    break
                max_steps = max(max_steps, 1 + dfs(j))
                
            for x in range(1, d + 1):
                j = i - x
                if j < 0 or arr[j] >= arr[i]:
                    break
                max_steps = max(max_steps, 1 + dfs(j))
                
            memo[i] = max_steps
            return max_steps

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
            
        return ans
            