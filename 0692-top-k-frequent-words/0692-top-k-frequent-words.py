class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq=Counter(words)
        words = sorted(freq.keys(), key=lambda x: (-freq[x], x))
        return words[:k]