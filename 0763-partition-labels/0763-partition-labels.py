class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ends = {c: i for i, c in enumerate(s)}        
        curr, out = 0, [0]
        
        while curr < len(s):
            last = ends[s[curr]]
            while curr <= last:
                symb = s[curr]
                last = max(last, ends[symb])
                curr += 1
            out.append(curr)
        
        return [out[i]-out[i-1] for i in range(1, len(out))]