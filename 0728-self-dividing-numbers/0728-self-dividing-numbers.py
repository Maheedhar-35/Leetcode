class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        for i in range(left,right+1):
            if i < 10:
                res.append(i)
                continue
            string=list(set(str(i)))
            if "0" in string:
                continue
            c=0
            for j in string:
                if i%int(j)!=0:
                    break
                c+=1    
            if c==len(string):
                res.append(i)
        return res        
