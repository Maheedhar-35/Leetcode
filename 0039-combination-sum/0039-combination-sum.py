class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        def backtrack(remaining,current,start):
            if remaining==0:
                result.append(list(current))
                return
            if remaining<0:
                return
            for i in range(start,len(candidates)):
                current.append(candidates[i])
                backtrack(remaining-candidates[i],current,i)
                current.pop()
        backtrack(target,[],0)
        return result                    