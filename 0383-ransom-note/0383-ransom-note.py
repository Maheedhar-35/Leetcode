class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """ 
        magazine=list(magazine)
        ransomNote=list(ransomNote)
        temp_b = magazine
        intersection = [x for x in ransomNote if x in temp_b and not temp_b.remove(x)]
        if intersection==ransomNote:
            return True
        return False    