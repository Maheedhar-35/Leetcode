class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s=="":
            return t
        s=list(s)
        t=list(t)
        for i in s:
            if i in t:
                t.pop(t.index(i))
        return t[0]        