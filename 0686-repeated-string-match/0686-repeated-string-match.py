class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        result = (len(b) + len(a) - 1) // len(a)

        curr = a * result
        if b in curr:
            return result
            
        curr += a
        if b in curr:
            return result + 1
            
        return -1