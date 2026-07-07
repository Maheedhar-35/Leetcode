class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        smax=nums[0]
        currmax=nums[0]
        for i in range(1,len(nums)):
            currmax=max(nums[i],currmax+nums[i])
            if currmax>smax:
                smax=currmax
        return smax        
