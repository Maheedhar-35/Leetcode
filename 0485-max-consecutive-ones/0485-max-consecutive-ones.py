class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mone=0
        count=0
        for i in nums:
            if i ==1:
                count+=1
            else:
                mone=max(mone,count)
                count=0
        mone=max(mone,count)        
        return mone            