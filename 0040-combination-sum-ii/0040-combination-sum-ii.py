class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates.sort()
        def backtrack(remaining,current,start):
            if remaining==0:
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
        backtrack(target,[],0)
        return result         