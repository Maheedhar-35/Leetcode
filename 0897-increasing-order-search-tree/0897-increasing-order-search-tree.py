# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        result = TreeNode(0)
        self.current = result
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            root.left = None
            self.current.right = root
            self.current = root
            inorder(root.right)
            
        inorder(root)
        return result.right