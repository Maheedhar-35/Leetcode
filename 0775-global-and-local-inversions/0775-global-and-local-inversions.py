class Solution(object):
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mx=0
        for i in range(len(nums)-2):
            mx=max(mx,nums[i])
            if mx>nums[i+2] :
                return False
        return True