class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates=[1,2,3,4,5,6,7,8,9]
        def backtrack(remaining,current,start):
            if remaining==0:
                if len(current)==k:
                    result.append(list(current))
                return
            if remaining<0:
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                backtrack(remaining-candidates[i],current,i+1)
                current.pop()
        backtrack(n,[],0)
        return result         