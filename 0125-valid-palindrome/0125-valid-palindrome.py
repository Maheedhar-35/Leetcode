class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0 or len(s)==1:
            return True
        s=s.lower()
        t=[char for char in s if char.isalnum()]
        if t==t[::-1]:
            return True
        return False    

    