class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n=len(candyType)
        candyset=list(set(candyType))
        if len(candyset)<n//2:
            return len(candyset)
        else:
            return n//2    