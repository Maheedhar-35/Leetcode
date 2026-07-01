class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        result =start ^ goal
        distance = 0
        
        while result > 0:
            result &= (result - 1)  
            distance += 1
            
        return distance