# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:       
            row = rand7()
            col = rand7()
            
            val = (row - 1) * 7 + col
        
            if val <= 40:
                return (val - 1) % 10 + 1