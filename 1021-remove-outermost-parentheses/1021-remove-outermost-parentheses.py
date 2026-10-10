class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=="" :
            return ""
        req=[]
        ocount=0
        ccount=0
        start=0
        for i in range(len(s)):
            if s[i]=="(":
                ocount+=1
            elif s[i]==")":
                ccount+=1
            if ocount==ccount:
                end=i
                req.append(s[start:end+1])
                start=i+1
        for i in range(len(req)) :
            req[i]=req[i][1:len(req[i])-1]
        return "".join(req)    