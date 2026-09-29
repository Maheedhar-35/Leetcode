class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        new=[]
        for i in range(len(matrix)):
            new.append([])
            for j in range(len(matrix)):
                new[i].append(matrix[i][j])
        for i in range(len(matrix)):
            k=len(matrix)-1
            j=0
            while k>=0:
                matrix[i][j]=new[k][i]
                j+=1
                k-=1
        print(new)