class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n ^ (n >> 1)
        
        return (num & (num + 1)) == 0