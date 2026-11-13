class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 1
        val=0
        for i in range(len(nums)-1):
            num=1
            k=nums[i]
            for j in range(i+1,len(nums)):
                if k>nums[j]:
                    k=nums[j]
                    num+=1
                else:
                    break
            val=max(val,num)
        for i in range(len(nums)-1):
            num=1
            k=nums[i]
            for j in range(i+1,len(nums)):
                if k<nums[j]:
                    k=nums[j]
                    num+=1
                else:
                    break
            val=max(val,num)
        return val
                