class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=num
        num=list(str(num))
        while len(num)>1:
            s=0
            s=sum(int(n) for n in num)
            num=list(str(s))
        return s    