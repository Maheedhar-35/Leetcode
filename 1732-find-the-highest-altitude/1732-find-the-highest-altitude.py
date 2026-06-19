class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        M=0
        alti=0
        for i in gain:
            alti+=i
            if alti>M:
                M=alti
        return M        