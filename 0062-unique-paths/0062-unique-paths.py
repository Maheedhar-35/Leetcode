class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def fact(n):
            if n<2:
                return 1
            return n*fact(n-1) 
        num=fact(m+n-2)
        den=fact(m-1)*fact(n-1)
        t=num/den
        return t       