class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if 1 not in bits :
            return True
        pair=[]   
        for i in bits:
            if len(pair)==2:
                pair=[]
            if i==1:
                pair.append(i)
            elif i==0 and len(pair)==1:
                pair.append(i)
        return pair==[]            
