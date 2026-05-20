class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count=0
        rng=[-1,-1]
        
        if target in nums:
            st=nums.index(target)
            for i in range(len(nums)):
                if nums[i]==target:
                    count=count+1
            return [st,st+count-1]
        else:
            return rng            
