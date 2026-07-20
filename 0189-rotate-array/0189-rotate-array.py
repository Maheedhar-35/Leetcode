class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        rem=k%len(nums)
        arr1=nums[len(nums)-rem:]
        arr2=nums[:len(nums)-rem]
        nums[:]=arr1+arr2
        return nums