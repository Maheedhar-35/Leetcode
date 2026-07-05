class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        result=[]
        srt=sorted(score)
        srt=srt[::-1]
        for i in score:
            if srt.index(i)==0:
                result.append("Gold Medal")
            elif srt.index(i)==1:
                result.append("Silver Medal")    
            elif srt.index(i)==2:
                result.append("Bronze Medal")   
            else:
                result.append(str(srt.index(i)+1)) 
        return result   