class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        lst2=lst1[::-1]
        lst=list(s)
        count=0
        val=0
        for let in lst:
            count+=(lst2.index(let)+1)*(val+1)
            val+=1
        return count    