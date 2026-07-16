class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
        if (presses == 0): 
            return 1
        elif (n == 1) :
            return 2
        elif (n == 2 and presses == 1) :
            return 3
        elif (n == 2 or presses == 1) :
            return 4
        elif (presses == 2) :
            return 7
        else :
            return 8