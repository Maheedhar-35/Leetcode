class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sumdig(num):
            s=0
            while num>0:
                s+=num%10
                num=num/10
            return s
        t=-1    
        for i in range(len(nums)):
            if sumdig(nums[i])==i :
                t=i
                break
        return t            