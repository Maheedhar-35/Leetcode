class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        step = 1
        remaining = n
        left_to_right = True
        
        while remaining > 1:
            if left_to_right or (remaining % 2 == 1):
                head += step
                
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right
            
        return head