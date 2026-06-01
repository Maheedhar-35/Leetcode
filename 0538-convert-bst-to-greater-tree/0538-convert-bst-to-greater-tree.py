# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.s=0
        def trav(root):
            if not root:
                return 
            trav(root.right)
            self.s+=root.val
            root.val=self.s
            trav(root.left)
        trav(root)    
        return root  