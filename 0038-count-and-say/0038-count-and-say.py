class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
            
        st = "1"
        for i in range(2, n + 1):
            next_st = []
            i = 0
            
            while i < len(st):
                count = 1
                while i + 1 < len(st) and st[i] == st[i + 1]:
                    count += 1
                    i += 1
                
                next_st.append(str(count))
                next_st.append(st[i])
                
                i += 1

            st = "".join(next_st)
            
        return st