class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        greater_map = {}
        stack = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                popped_element = stack.pop()
                greater_map[popped_element] = num
            
            stack.append(num)
            
        while stack:
            popped_element = stack.pop()
            greater_map[popped_element] = -1
            
        return [greater_map[x] for x in nums1]