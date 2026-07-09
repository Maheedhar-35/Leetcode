class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        count=Counter(nums)
        for i in range(n):
            if count[i+1]==2:
                result1=[]
                result1.append(i+1)
            if i+1 not in nums:
                result2=[]
                result2.append(i+1)    
        return result1+result2        