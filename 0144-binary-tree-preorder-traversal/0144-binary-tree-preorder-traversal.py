# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        count=[]
        def pre(root): 
            if root==None:
                return 
            count.append(root.val)
            pre(root.left)
            pre(root.right)
        pre(root)
        return count        
