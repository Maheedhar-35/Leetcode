class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        left = 0
        right = len(chars) - 1
        
        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
                
            while left < right and chars[right] not in vowels:
                right -= 1
                
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                # Step inward
                left += 1
                right -= 1
        return "".join(chars)