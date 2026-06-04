class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def wave(num):
            if num<101:
                return 0
            num=str(num)
            s=list(num)  
            count=0
            for i in range(1,len(s)-1):
                if int(s[i])>int(s[i-1]) and int(s[i])>int(s[i+1]):
                    count+=1
                if int(s[i])<int(s[i-1]) and int(s[i])<int(s[i+1]):
                    count+=1       
            return count        
        c=0
        for i in range(num1,num2+1):
            c=c+wave(i)
        return c        