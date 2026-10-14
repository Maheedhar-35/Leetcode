class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum >num*9:
            return ""
        result=[]
        while sum>0:
            if sum>9:
                result.append("9")
                sum-=9
            else:
                result.append(str(sum))
                sum=0
        while len(result)<num:
            result.append("0")
        return "".join(result)