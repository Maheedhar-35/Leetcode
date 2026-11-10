class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        
        st = nums.index(0)
        
        inc = True
        for j in range(n - 1):
            if (nums[j] + 1) % n != nums[j + 1]:
                inc = False
                break
                
        if inc:
            return min(st, n - st +2)
        
        dec = True
        for j in range(n - 1):
            if (nums[j] - 1 + n) % n != nums[j + 1]:
                dec = False
                break
                
        if dec:
            return min(n - st, st + 2)
            
        return -1