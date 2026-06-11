import string
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result=[]
        count=list(string.ascii_uppercase)
        while columnNumber>0:
            columnNumber-=1
            result.append(count[columnNumber%26])
            columnNumber=columnNumber//26
        return "".join(result[::-1])    
