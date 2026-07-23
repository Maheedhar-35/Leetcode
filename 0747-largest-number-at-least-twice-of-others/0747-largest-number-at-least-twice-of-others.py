class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=sorted(nums)
        print(nums)
        return nums.index(num[-1]) if num[-1]>=num[-2]*2 else -1