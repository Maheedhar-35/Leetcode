class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = defaultdict(list)
        
        for s in strs:
            sorted_key = "".join(sorted(s))
            anagram[sorted_key].append(s)
        return list(anagram.values())