# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        count=[]
        def trav(root):
            if root is None :
                return
            trav(root.left)
            count.append(root.val)
            trav(root.right)
        trav(root)
        s=sum(x for x in count if x>=low and x<=high) 
        return s       