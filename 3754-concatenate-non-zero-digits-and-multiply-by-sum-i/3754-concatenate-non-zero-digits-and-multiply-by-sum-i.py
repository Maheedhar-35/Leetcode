class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        res=list(str(n))
        dig=[x for x in res if x!="0"]
        tot=sum(int(x) for x in res)
        return int("".join(dig))*tot