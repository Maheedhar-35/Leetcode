class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s=sum(nums)
        
        if not s%2==0:
            return False
        target=s//2
        dp={0}
        for num in nums:
            next_dp = {current_sum + num for current_sum in dp if current_sum + num <= target}
            dp.update(next_dp)
            if target in dp :
                return True
        return target in dp        