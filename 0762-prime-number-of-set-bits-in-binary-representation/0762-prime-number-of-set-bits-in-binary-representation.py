class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prime=[2,3,5,7,11,13,17,19]
        c=0
        for i in range(left,right+1):
            binarydig=bin(i)[2:]
            tot=sum(int(x) for x in binarydig)
            if int(tot) in prime:
                c+=1
        return c        