class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        
        low = 0
        high = nums[-1] - nums[0]
        
        def countPairs(mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += (right - left)
            return count

        while low < high:
            mid = (low + high) // 2
            if countPairs(mid) >= k:
                high = mid 
            else:
                low = mid + 1 
                
        return low