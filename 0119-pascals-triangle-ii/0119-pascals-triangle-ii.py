class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tri=[]
        for rownum in range(rowIndex+1):
            row=[1]*(rownum+1)
            for j in range(1,rownum):
                row[j]=tri[rownum-1][j-1]+tri[rownum-1][j]
            tri.append(row)
        return tri[rowIndex]        