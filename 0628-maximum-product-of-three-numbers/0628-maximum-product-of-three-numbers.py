class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        first=nums[0]*nums[1]*nums[-1]
        last=nums[-1]*nums[-2]*nums[-3]
        return max(first,last)