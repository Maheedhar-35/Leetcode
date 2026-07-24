class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        s=0   
        for i in range(len(jewels)):
            c=0
            for j in stones:
                if jewels[i]==j:
                    c+=1
            s+=c
        return s   