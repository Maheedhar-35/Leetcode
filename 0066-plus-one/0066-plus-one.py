class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        n=len(digits)
        for i in range(len(digits)):
            num= 10*num+digits[i]   
        digits=[]
        num=num+1
        while num>0:
            digits=[num%10] +digits
            num=num//10
        return digits           