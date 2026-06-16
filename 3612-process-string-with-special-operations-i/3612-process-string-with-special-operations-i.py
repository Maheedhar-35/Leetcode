import string
class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=[]
        s=list(s)
        count=list(string.ascii_lowercase)
        for i in s:
            if i in count:
                result.append(i)
                continue
            if i=="*":
                if result!=[]:      
                    result.pop()
                continue
            if i=="#":
                result=result*2
                continue
            if i=="%" :
                result=result[::-1]
        return "".join(result)           