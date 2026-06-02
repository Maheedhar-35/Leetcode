# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        count=[]
        def trav(root):
            if root is None :
                return 
            trav(root.left)
            count.append(root.val)
            trav(root.right)
        trav(root)
        for i in count:
            for j in count:
                if i+j==k and i!=j:
                    return True
        return False            
