class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst=list(str(n))
        max1=max(lst)
        lst.remove(max1)
        max2=max(lst)
        return int(max1)*int(max2)