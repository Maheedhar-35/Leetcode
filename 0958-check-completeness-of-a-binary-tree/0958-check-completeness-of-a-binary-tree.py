# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None :
            return True 
        queue = collections.deque([root])
        t = False
        
        while queue:
            node = queue.popleft()
            
            if node is None:
                t = True
            else:
                if t:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True    
