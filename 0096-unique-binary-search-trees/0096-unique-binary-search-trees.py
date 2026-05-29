class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(x) :
            if x==0 or x==1:
                return 1
            return x*f(x-1)
        return (f(2*n)/(f(n)*f(n+1)))        