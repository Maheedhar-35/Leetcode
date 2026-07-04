class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = []
        count = 0
    
        for char in reversed(s):
            if char != '-':
                if count == k:
                    result.append('-')
                    count = 0
            
                result.append(char.upper())
                count += 1
            
        return "".join(reversed(result))