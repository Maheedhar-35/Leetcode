class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        
        longest = 0
        current = float('-inf')
        
        for left, right in pairs:
            if left > current:
                longest += 1
                current = right
                
        return longest