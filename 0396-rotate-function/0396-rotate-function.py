class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        S = sum(nums)
        curr = sum(i * x for i, x in enumerate(nums))
        Max = curr
        for k in range(1, n):
            curr = curr + S - n * nums[n - k]
            if curr > Max:
                Max = curr

        return Max