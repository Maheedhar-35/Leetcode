class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(index, current_subset):
            result.append(list(current_subset))
            
            for i in range(index, len(nums)):
                current_subset.append(nums[i])
                
                backtrack(i + 1, current_subset)
                
                current_subset.pop()
                
        backtrack(0, [])
        return result