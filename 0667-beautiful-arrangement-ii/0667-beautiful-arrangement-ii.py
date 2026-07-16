class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        nums=[x for x in range(1,n+1)]
        for i in range(k):
            nums = nums[:i] + nums[i:][::-1]
        return nums