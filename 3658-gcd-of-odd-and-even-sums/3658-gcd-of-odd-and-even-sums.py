class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        oddsum=n**2
        evensum=n*(n+1)
        return n