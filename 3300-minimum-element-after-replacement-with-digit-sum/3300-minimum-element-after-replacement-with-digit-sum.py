class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=[]
        n=len(nums)
        for i in range(n):
            st=[]
            nums[i]=str(nums[i])
            st=list(nums[i])
            st=list(map(int,st))
            c.append(sum(st))
        return min(c)    