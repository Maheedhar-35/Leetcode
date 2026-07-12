class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        nums=sorted(list(set(arr)))
        rankmap = {num: rank for rank, num in enumerate(nums, 1)}
        return [rankmap[x] for x in arr]