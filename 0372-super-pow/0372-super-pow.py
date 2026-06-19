class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337
        if not b:
            return 1
        def normal_pow(base, exp):
            base %= MOD
            res = 1
            for _ in range(exp):
                res = (res * base) % MOD
            return res
        last_digit = b.pop()
        part1 = normal_pow(a, last_digit)
        part2 = normal_pow(self.superPow(a, b), 10)
        return (part1 * part2) % MOD