class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if not digits:
            return result
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl','6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'} 
        def backtrack(index, current):
            if index == len(digits):
                result.append("".join(current))
                return
            current_digit = digits[index]
            possible_letters = phone[current_digit]
            
            for letter in possible_letters:
                current.append(letter)
                backtrack(index + 1, current)
                current.pop()
                
        backtrack(0, [])
        return result