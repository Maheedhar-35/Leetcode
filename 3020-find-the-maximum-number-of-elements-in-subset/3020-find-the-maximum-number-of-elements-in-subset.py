class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        max_subset_len = 0
        
        if 1 in counts:
            c = counts[1]
            max_subset_len = c if c % 2 != 0 else c - 1
            
        for x in counts:
            if x == 1:
                continue
                
            current_len = 0
            curr = x
            
            while True:
                if counts[curr] >= 2:
                    current_len += 2
                    curr = curr * curr 
                elif counts[curr] == 1:
                    current_len += 1
                    break
                else:
                    current_len -= 1
                    break
                    
            max_subset_len = max(max_subset_len, current_len)
            
        return max_subset_len