class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums=[]
        a=0
        b=0
        while a<m and b<n:
            if nums1[a]<=nums2[b]:
                nums.append(nums1[a])
                a=a+1
            else:
                nums.append(nums2[b])
                b=b+1    
        while a < m:
            nums.append(nums1[a])
            a += 1
            
        while b < n:
            nums.append(nums2[b])
            b += 1   

        nums1[:]=nums        