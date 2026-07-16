class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b) 

        prefix_gcd = []
        mx = 0
    
        for x in nums:
            if x > mx:
                mx = x
            prefix_gcd.append(gcd(x, mx))
            
        prefix_gcd.sort()
        
        result = 0
        for i in range(n // 2):
            result += gcd(prefix_gcd[i], prefix_gcd[n - 1 - i])
            
        return result