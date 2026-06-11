import string
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        count=list(string.ascii_uppercase)
        s=list(columnTitle)
        sum=0
        for i in s:
            sum=sum*26+(count.index(i)+1)
        return sum