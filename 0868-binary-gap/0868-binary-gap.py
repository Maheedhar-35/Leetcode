class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        curr=0
        bindig=bin(n)[2:]
        if bindig.count("1")==1:
            return 0
        for i in bindig:
            if i=="0":
                curr+=1
            else:
                curr+=1
                c=max(curr,c)
                curr=0
            
        return c            
