# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result=[]
        def trav(root,level,index):
            if root is None:
                return
            if level==len(result) :
                result.append([])
            result[level].append(index)
            trav(root.left,level+1,2*index)
            trav(root.right,level+1,2*index+1)
        trav(root,0,1)
        m=0
        for i in result:
            width=i[-1]-i[0]+1
            if m<width:
                m=width
        return m        