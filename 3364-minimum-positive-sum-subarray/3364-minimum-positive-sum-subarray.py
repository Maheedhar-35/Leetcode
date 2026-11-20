class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        s=float("inf")
        c=0
        while l<=r:
            for i in range(len(nums)-l+1):
                if sum(nums[i:i+l])>0:
                    s=min(s,sum(nums[i:i+l]))
                    c+=1
            l+=1
        if c>0:
            return s    
        else:
            return -1
            