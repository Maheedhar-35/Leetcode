class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result=0
        k=nums[len(nums)//2]
        for i in range(len(nums)):
            result+=abs(nums[i]-k)
        return result    