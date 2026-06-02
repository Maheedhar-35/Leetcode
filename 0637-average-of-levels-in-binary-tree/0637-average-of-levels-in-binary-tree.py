# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        result = []
        
        def preorder(node,level):
            if not node:
                return
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            preorder(node.left,level + 1)
            preorder(node.right,level + 1)
        preorder(root, 0)
        avg=[]
        for i in result:
            avg.append(float(sum(i))/len(i))
        return avg    