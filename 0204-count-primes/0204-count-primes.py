class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0

        prime = [1] * (n)
        p = 2
        prime[0],prime[1]=0,0
        
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n, p):
                    prime[i] = 0
            p += 1
        return sum(prime)