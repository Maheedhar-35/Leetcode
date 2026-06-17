class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lengths = []
        current_length = 0
        
        for i in s:
            if i.islower():
                current_length += 1
            elif i == "*":
                if current_length > 0:
                    current_length -= 1
            elif i == "#":
                current_length *= 2
            elif i == "%":
                pass 
                
            lengths.append(current_length)
            if current_length > k * 2 and i == "#":
                pass 

        if k >= current_length:
            return "."

        for i in range(len(s) - 1, -1, -1):
            op = s[i]
            length_before_op = lengths[i-1] if i > 0 else 0
            
            if op == "%":
                current_length = lengths[i]
                if current_length > 0:
                    k = current_length - 1 - k
                    
            elif op == "#":
                half_length = length_before_op
                if half_length > 0:
                    k %= half_length
                current_length = half_length
                
            elif op == "*":
                current_length = length_before_op
                
            elif op.islower():
                if k == current_length - 1:
                    return op
                current_length -= 1
                
        return "."