class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result=[]
        for i in operations:
            if i=="+":
                s=result[-1]+result[-2]
                result.append(s)
            elif i=="D":
                result.append(2*result[-1])
            elif i=="C":
                result.pop()
            else:
                result.append(int(i))

        return sum(result)                