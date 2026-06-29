class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)
        
        total_sum = sum(nums)
    
        return total_sum - len(nums) * min_val