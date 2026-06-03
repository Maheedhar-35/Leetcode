class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        n = len(landStartTime)
        m = len(waterStartTime)
        lands = []
        for i in range(n):
            lands.append((landStartTime[i], landDuration[i], landStartTime[i] + landDuration[i]))
            
        waters = []
        for j in range(m):
            waters.append((waterStartTime[j], waterDuration[j], waterStartTime[j] + waterDuration[j]))
        lands.sort(key=lambda x: x[0])
        waters.sort(key=lambda x: x[0])
        
        ans = float('inf')
        def solve_half(category_A, category_B):
            len_B = len(category_B)
            min_B_total_suffix = [float('inf')] * (len_B + 1)
            min_B_dur_suffix = [float('inf')] * (len_B + 1)
            
            for k in range(len_B - 1, -1, -1):
                min_B_total_suffix[k] = min(min_B_total_suffix[k+1], category_B[k][2])
                min_B_dur_suffix[k] = min(min_B_dur_suffix[k+1], category_B[k][1])
                
            best_finish = float('inf')
            b_idx = 0
            
            min_A_finish_valid = float('inf')
            for a_start, a_dur, a_finish in category_A:
                low, high = 0, len_B
                while low < high:
                    mid = (low + high) // 2
                    if category_B[mid][0] > a_finish:
                        high = mid
                    else:
                        low = mid + 1
                if low < len_B:
                    best_finish = min(best_finish, min_B_total_suffix[low])
            category_A_by_finish = sorted(category_A, key=lambda x: x[2])
            b_ptr = 0
            min_b_dur = float('inf')
            
            for a_start, a_dur, a_finish in category_A_by_finish:
                while b_ptr < len_B and category_B[b_ptr][0] <= a_finish:
                    min_b_dur = min(min_b_dur, category_B[b_ptr][1])
                    b_ptr += 1
                if min_b_dur != float('inf'):
                    best_finish = min(best_finish, a_finish + min_b_dur)
                    
            return best_finish
        ans = min(ans, solve_half(lands, waters))
        ans = min(ans, solve_half(waters, lands))
        
        return ans