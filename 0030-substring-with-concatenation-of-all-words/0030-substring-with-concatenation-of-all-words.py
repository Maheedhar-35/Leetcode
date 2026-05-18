class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
            
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        s_len = len(s)
        
        word_freq = Counter(words)
        result = []
        
        for i in range(word_len):
            left = i
            right = i
            current_count = {}
            words_used = 0
            
            while right + word_len <= s_len:
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_freq:
                    current_count[word] = current_count.get(word, 0) + 1
                    words_used += 1
                    
                    while current_count[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                    
                    if words_used == word_count:
                        result.append(left)
                        
                else:
                    current_count.clear()
                    words_used = 0
                    left = right
                    
        return result
            