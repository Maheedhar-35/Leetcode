class Solution(object):
    def findSubstringInWraproundString(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        dp = [0] * 26
        
        current_max_len = 0
        
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25):
                current_max_len += 1
            else:
                current_max_len = 1
                
            char_idx = ord(s[i]) - ord('a')
            
            dp[char_idx] = max(dp[char_idx], current_max_len)
            
        return sum(dp)