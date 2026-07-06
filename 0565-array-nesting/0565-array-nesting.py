class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len=0
        visited = [False] * len(nums)
        
        for i in range(len(nums)):
            if visited[i]:
                continue
                
            current_len = 0
            t = i
            
            while not visited[t]:
                visited[t] = True  
                t = nums[t]        
                current_len += 1   
                
            max_len = max(max_len, current_len)
        return max_len       