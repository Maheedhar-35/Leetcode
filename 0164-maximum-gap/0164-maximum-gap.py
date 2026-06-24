class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0 or len(nums)==1:
            return 0
        nums.sort()
        mx=0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>mx:
                mx=nums[i]-nums[i-1]
        return mx        