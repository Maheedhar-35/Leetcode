class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        """
        :type s: str
        :rtype: bool
        """
        digits=list(s)
        for i in range(1,len(digits)):
            if abs(int(digits[i])-int(digits[i-1]))>2 :
                return False
        else:
            return True