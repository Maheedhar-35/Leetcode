class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
            
        hex_map = "0123456789abcdef"
        
        num &= 0xFFFFFFFF
        
        result = []
        
        while num > 0:
            last_four_bits = num & 15
            result.append(hex_map[last_four_bits])
            
            num >>= 4
            
        return "".join(result[::-1])