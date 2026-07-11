class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)-1):
            
            if target-nums[i] in nums[i+1:]:
                lst=nums[i+1:]
                comp=target-nums[i]
                return [i,i+1+lst.index(comp)]
