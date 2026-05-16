class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        string = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in string:
                last = stack.pop() if stack else '!'
                if string[char] != last:
                    return False
            else:
                stack.append(char)
        return not stack    
