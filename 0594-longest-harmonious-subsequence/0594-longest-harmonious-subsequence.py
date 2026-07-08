class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        maxlen = 0
        
        for num in counts:
            if num + 1 in counts:
                currlen = counts[num] + counts[num + 1]
                maxlen = max(maxlen, currlen)
                
        return maxlen