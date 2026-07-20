class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total = m * n
        
        arr = []
        for row in grid:
            arr.extend(row)
            
        k = k % total
        
        rotated = arr[total - k:] + arr[:total - k]
        
        result = []
        for i in range(0, total, n):
            result.append(rotated[i : i + n])
            
        return result