class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t1=len(nums)
        st=set(nums)
        result=sorted(list(st))
        t2=len(result) 
        for i in range (0,t1-len(result)):
            result.append('_')  
        nums[:]=result  
        return t2     

        