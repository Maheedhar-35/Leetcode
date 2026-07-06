class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count("A")>1:
            return False
        count=0    
        for i in s:
            if i=="L":
                count+=1
            else:
                count=0 
            if count>=3:
                return False
        return True                   