class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        nums=list(str(n))
        val=1
        for i in nums:
            val=val*int(i)
        while val%t!=0:
            n+=1
            nums=list(str(n))
            val=1
            for i in nums:
                val=val*int(i)
        return n        
                