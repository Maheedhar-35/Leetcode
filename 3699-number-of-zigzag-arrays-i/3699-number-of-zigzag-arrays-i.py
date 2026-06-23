class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        K = r - l + 1
        
        if K <= 1 or n < 3:
            return 0
            
        up = [v for v in range(K)]
        down = [K - 1 - v for v in range(K)]
        
        for _ in range(3, n + 1):
            next_up = [0] * K
            next_down = [0] * K
            
            prefix_down = 0
            for v in range(K):
                next_up[v] = prefix_down % MOD
                prefix_down += down[v]
                
            suffix_up = 0
            for v in range(K - 1, -1, -1):
                next_down[v] = suffix_up % MOD
                suffix_up += up[v]
                
            up = next_up
            down = next_down
            
        return (sum(up) + sum(down)) % MOD