class Solution(object):
    def maxDigitRange(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def Drange(num):
            digits = str(num)
            return int(max(digits)) - int(min(digits))    
        max_range = max(Drange(num) for num in nums)
    
        return sum(num for num in nums if Drange(num) == max_range)