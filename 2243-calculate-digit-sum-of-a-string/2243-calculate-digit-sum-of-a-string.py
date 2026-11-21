class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s)>k:
            res = []
            for i in range(0,len(s),k):
                grp = s[i:i+k]
                summ = sum(int(digit) for digit in grp)
                res.append(str(summ))
            s = "".join(res)
        return s