class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        gmax=nums[0]
        currmax=nums[0]
        currmin=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                currmax ,currmin=currmin,currmax
            currmax=max(nums[i],currmax*nums[i])
            currmin=min(nums[i],currmin*nums[i])
            gmax=max(gmax,currmax)
        return gmax        