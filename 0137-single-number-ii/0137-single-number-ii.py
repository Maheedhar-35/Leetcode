class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=list(set(nums))
        for i in s:
            count=0
            for j in nums:
                if i==j:
                    count+=1   
            if count==1:
                return i         