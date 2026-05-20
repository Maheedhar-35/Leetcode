class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        rtype = []
        s = set()
        count = 0
        
        for i in range(n):
            if A[i] in s:
                count += 1
            else:
                s.add(A[i])
                
            if B[i] in s:
                count += 1
            else:
                s.add(B[i])
                
            rtype.append(count)
            
        return rtype