class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        req=[]
        val=0
        for i in range(len(nums)):
            for j in range(0,len(nums)-i):
                req=nums[j:j+i+1]
                val+=(len(list(set(req))))**2
        return val