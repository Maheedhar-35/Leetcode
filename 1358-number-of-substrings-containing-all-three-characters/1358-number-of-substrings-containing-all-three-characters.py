class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {'a': 0, 'b': 0, 'c': 0}
        
        left = 0
        substrings = 0
        
        for right in range(len(s)):
            counts[s[right]] += 1
            
            while counts['a'] > 0 and counts['b'] > 0 and counts['c'] > 0:
                substrings += (len(s) - right)
                
                counts[s[left]] -= 1
                left += 1
                
        return substrings