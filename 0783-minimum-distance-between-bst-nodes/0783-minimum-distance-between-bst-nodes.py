# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        count=[]    
        def trav(root):
            if root is None:
                return 
            trav(root.left)
            count.append(root.val)
            trav(root.right)
        trav(root)
        m=float('inf')
        for i in range(len(count)-1):
            if count[i+1]-count[i]<m:
                m=count[i+1]-count[i]
        return m        
