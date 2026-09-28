class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def good(t):
            lst=list(str(t))
            if '3' in lst or '4' in lst or '7' in lst:
                return 0      
            else:
                for i in range(len(lst)):
                    if lst[i]=='2':
                        lst[i]='5'    
                    elif lst[i]=='5':
                        lst[i]='2'  
                    elif lst[i]=='6':
                        lst[i]='9'   
                    elif lst[i]=='9':
                        lst[i]='6'         
                st="".join(lst)
                return st!=str(t)        
        count=0
        for i in range(1,n+1):
            count+=good(i)
        return count    
            