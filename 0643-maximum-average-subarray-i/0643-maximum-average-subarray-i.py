class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        currsum = sum(nums[:k])
        maxsum = currsum
        
        for i in range(k, len(nums)):
            currsum += nums[i] - nums[i - k]
            
            if currsum > maxsum:
                maxsum = currsum
                
        return float(maxsum) / k