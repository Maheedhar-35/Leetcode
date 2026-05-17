class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_len = len(needle)
        h_len = len(haystack)
        if n_len > h_len:
            return -1
            
        for i in range(h_len - n_len + 1):
            if haystack[i : i + n_len] == needle:
                return i
                
        return -1