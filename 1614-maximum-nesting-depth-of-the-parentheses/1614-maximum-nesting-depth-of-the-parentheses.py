class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=0
        left=0
        right=0
        for i in s:
            if i=="(":
                left+=1
            elif i==")":
                right+=1
            m=max(m,left-right) 
        return m           