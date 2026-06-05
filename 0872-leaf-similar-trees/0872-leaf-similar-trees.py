# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        count1=[] 
        count2=[]
        def trav(root,count):
            if root is None:
                return
            trav(root.left,count)
            if root.right==None and root.left==None:
                count.append(root.val)
            trav(root.right,count)
        trav(root1,count1)    
        trav(root2,count2)
        if count1==count2:
            return True
        return False    