class Solution(object):
    def countKthRoots(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        def get_max_root(n):
            if n < 0:
                return -1
            if n == 0:
                return 0
            ans = int(n ** (1.0 / k))
            while (ans + 1) ** k <= n:
                ans += 1
            while ans ** k > n:
                ans -= 1
                
            return ans

        return get_max_root(r) - get_max_root(l - 1)