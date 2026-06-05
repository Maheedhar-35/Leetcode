class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def count_up_to(limit_str):
            n = len(limit_str)
            memo = {}
            
            def dp(idx, prev2, prev1, is_less, is_started):
                if idx == n:
                    return 0
                    
                state = (idx, prev2, prev1, is_less, is_started)
                if state in memo:
                    return memo[state]
                    
                limit_digit = int(limit_str[idx])
                upper_bound = 9 if is_less else limit_digit
                
                total_waviness = 0
                
                for d in range(upper_bound + 1):
                    next_is_less = is_less or (d < limit_digit)
                    
                    if not is_started:
                        if d == 0:
                            total_waviness += dp(idx + 1, -1, -1, next_is_less, False)
                        else:
                            total_waviness += dp(idx + 1, -1, d, next_is_less, True)
                    else:
                        is_wave = 0
                        if prev2 != -1:
                            if prev1 > prev2 and prev1 > d:
                                is_wave = 1
                            elif prev1 < prev2 and prev1 < d:
                                is_wave = 1
                        if is_wave == 1:
                            total_waviness += count_suffixes(idx + 1, next_is_less)
                            
                        total_waviness += dp(idx + 1, prev1, d, next_is_less, True)
                        
                memo[state] = total_waviness
                return total_waviness

            suffix_memo = {}
            def count_suffixes(idx, is_less):
                if idx == n:
                    return 1
                state = (idx, is_less)
                if state in suffix_memo:
                    return suffix_memo[state]
                
                limit_digit = int(limit_str[idx])
                upper_bound = 9 if is_less else limit_digit
                
                ways = 0
                for d in range(upper_bound + 1):
                    next_is_less = is_less or (d < limit_digit)
                    ways += count_suffixes(idx + 1, next_is_less)
                    
                suffix_memo[state] = ways
                return ways

            return dp(0, -1, -1, False, False)

        ans_num2 = count_up_to(str(num2))
        ans_num1 = count_up_to(str(num1 - 1)) if num1 > 0 else 0
        
        return ans_num2 - ans_num1