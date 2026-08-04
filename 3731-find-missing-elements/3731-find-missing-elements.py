class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(min(nums)+1,max(nums)):
            if i not in nums:
                res.append(i)
        return res        