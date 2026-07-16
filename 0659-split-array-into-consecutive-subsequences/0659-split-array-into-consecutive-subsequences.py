class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}
        end = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        for x in nums:
            if count.get(x, 0) == 0:
                continue
                
            if end.get(x - 1, 0) > 0:
                end[x - 1] -= 1
                end[x] = end.get(x, 0) + 1
                count[x] -= 1
                
            elif count.get(x + 1, 0) > 0 and count.get(x + 2, 0) > 0:
                count[x] -= 1
                count[x + 1] -= 1
                count[x + 2] -= 1
                end[x + 2] = end.get(x + 2, 0) + 1
                
            else:
                return False
                
        return True