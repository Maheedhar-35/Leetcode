class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []
            
        m, n = len(mat), len(mat[0])
        diagonals = [[] for x in range(m + n - 1)]
        
        for r in range(m):
            for c in range(n):
                diagonals[r + c].append(mat[r][c])
                
        result = []
        for i, diagonal in enumerate(diagonals):
            if i % 2 == 0:
                result.extend(reversed(diagonal))
            else:
                result.extend(diagonal)
                
        return result