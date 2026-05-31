class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids=sorted(asteroids)
        count=mass
        for i in range(len(asteroids)):
            if count>=asteroids[i]:
                count+=asteroids[i]
            else:
                
                return False
        return True            