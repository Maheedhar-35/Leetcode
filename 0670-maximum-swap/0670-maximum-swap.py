class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits=list(str(num))
        for i in range(len(digits)):
            if digits[i]==max(digits[i:]):
                continue
            else:
                maxi=max(digits[i:])
                index = 0
                for j in range(len(digits) - 1, i - 1, -1):
                    if digits[j] == maxi:
                        index = j - i
                        break
                
                digits[i], digits[i+index] = digits[i+index], digits[i]
                break
        s="".join(digits)
        return int(s)       
                