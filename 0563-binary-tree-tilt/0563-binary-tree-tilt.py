# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.tilt = 0
        
        def subtree_sum(root):
            if not root:
                return 0
                
            left_sum = subtree_sum(root.left)
            right_sum = subtree_sum(root.right)
            root_tilt = abs(left_sum - right_sum)
            self.tilt += root_tilt
            return root.val + left_sum + right_sum
        subtree_sum(root)
        return self.tilt