class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        s=0
        p=2
        while n>1:
            while n%p==0:
                s+=p
                n=n//p
            p+=1    
        return s           