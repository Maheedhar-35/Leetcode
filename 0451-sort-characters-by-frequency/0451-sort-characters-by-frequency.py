class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = Counter(s)
        
        sorted_chars = counts.most_common()
        
        result = []
        for char, freq in sorted_chars:
            result.append(char * freq)
            
        return "".join(result)