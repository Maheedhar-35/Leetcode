class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        req=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    req.append([i,j])
        print(req)            
        if not req:
            return matrix
        for i in req:
            for a in range(len(matrix[0])):
                matrix[i[0]][a]=0
            for a in range(len(matrix)):
                matrix[a][i[1]]=0
        return matrix            
