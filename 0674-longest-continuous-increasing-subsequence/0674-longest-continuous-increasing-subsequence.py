class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr=1
        maxi=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                curr+=1
                maxi=max(maxi,curr)
            else:
                curr=1
        return maxi            