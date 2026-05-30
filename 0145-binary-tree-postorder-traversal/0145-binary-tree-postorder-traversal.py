# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        count=[]
        def post(root): 
            if root==None:
                return 
            post(root.left)
            post(root.right)
            count.append(root.val)
        post(root)
        return count        
