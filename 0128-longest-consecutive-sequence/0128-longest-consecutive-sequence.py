class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        nums=list(set(nums))
        nums.sort()
        max_streak = 1
        current_streak = 1
    
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 1
             
        return max(max_streak, current_streak)