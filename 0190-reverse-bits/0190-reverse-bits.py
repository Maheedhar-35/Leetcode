class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=[]
        i=0
        s=0
        while i<32 or n>0:
            if n>0:
                c.append(n%2)
                n=n//2
                i+=1
                s=s*2+c[i-1]
                continue
            c.append(0)
            i+=1
            s=s*2+c[i-1]
        return s        