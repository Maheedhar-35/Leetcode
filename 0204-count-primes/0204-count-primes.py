class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0

        prime = [True] * (n)
        p = 2
        prime[0]=False
        prime[1]=False
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1
        return sum(prime)