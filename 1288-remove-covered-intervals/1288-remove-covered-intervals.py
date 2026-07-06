class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        max_right = 0
        
        for left, right in intervals:
            if right > max_right:
                count += 1
                max_right = right 
                
        return count