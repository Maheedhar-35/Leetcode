class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        i =0 
        total = 0

        while total < target:
            i += 1
            total += i
        
        while (total - target) % 2 != 0:
            i += 1
            total += i

        return i