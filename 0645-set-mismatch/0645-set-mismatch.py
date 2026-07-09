class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        orginalsum = n * (n + 1) // 2
        givensum = sum(nums)
        uniquesum = sum(set(nums)) 
        
        duplicate = givensum - uniquesum
        missing = orginalsum - uniquesum
        
        return [duplicate, missing]