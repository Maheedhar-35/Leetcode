class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key=abs)
        first=0
        sec=0
        for i in range(len(nums)):
            if i<=len(nums)//2-1:
                first+=(nums[i])**2
            else:
                sec+=(nums[i])**2
        print(nums)        
        return sec-first            
