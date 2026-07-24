class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==1:
            return 0
        prev = self.kthGrammar(n - 1,(k + 1)//2)
        if k % 2 == 1:
            return prev
        else:
            return 1 if prev == 0 else 0