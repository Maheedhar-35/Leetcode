class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        result=abs((hour+(minutes/60.0))*30-minutes*6)
        return result if result<=180 else 360-result