class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        if n%2==0:
            return True
        ans=list(nums)
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                ans[j]=max(nums[i]-ans[j],nums[j]-ans[j-1])
        return ans[-1]>=0

