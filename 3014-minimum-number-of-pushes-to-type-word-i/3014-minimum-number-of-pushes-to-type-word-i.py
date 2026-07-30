class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        if len(word)<=8:
            return len(word)
        elif len(word)<=16:
            return (len(word)-8)*2+8
        elif len(word)<=24:
            return (len(word)-16)*3+8+8*2
        else:
            return 8+8*2+8*3+(len(word)-24)*4            
