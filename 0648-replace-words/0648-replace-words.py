class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        Set=set(dictionary)
        words=sentence.split()
        for i in range(len(words)):
            word = words[i]
            for j in range(1, len(word) + 1):
                prefix = word[:j]
                if prefix in Set:
                    words[i] = prefix
                    break
                    
        return " ".join(words)