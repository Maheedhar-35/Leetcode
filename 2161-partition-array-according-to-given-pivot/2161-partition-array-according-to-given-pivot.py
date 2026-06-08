class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        result1=[x for x in nums if x<pivot]
        result2=[x for x in nums if x==pivot]
        result3=[x for x in nums if x>pivot]    
        result=result1+result2+result3
        return result  