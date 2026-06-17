class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t=n
        while t>=1:
            if t==1:
                return True
            if t%4!=0:
                return False    
            t=float(t/4)
        return False        