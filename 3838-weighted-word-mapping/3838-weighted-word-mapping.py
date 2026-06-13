import string
class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        count=list(string.ascii_lowercase)
        result=[]
        for i in words:
            s=0
            for j in i:
                s+=weights[count.index(j)]
            result.append(count[25-s%26])   
        return "".join(result)     