class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        n = len(nums1)
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        max_diff = max(diff)
        if max_diff == 0:
            return 0
            
        counts = [0] * (max_diff + 1)
        for d in diff:
            counts[d] += 1
            
        tot = k1 + k2
        
        for v in range(max_diff, 0, -1):
            if counts[v] == 0:
                continue
                
            if tot >= counts[v]:
                tot -= counts[v]
                counts[v - 1] += counts[v] 
                counts[v] = 0
            else:
                counts[v - 1] += tot
                counts[v] -= tot
                tot = 0
                break 
                
        return sum(count * (v ** 2) for v, count in enumerate(counts))
