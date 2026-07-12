class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%3==0:
            if n>3:
                return 3**(n//3)
            else:
                return 2    
        elif n%3==1:
            return 4*(3**(n//3-1))
        else:
            if n>2:
                return 2*(3**(n//3))     
            else:
                return 1       