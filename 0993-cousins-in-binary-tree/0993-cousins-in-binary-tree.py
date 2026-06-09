# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.x = None
        self.y = None
        
        def dfs(node, depth, parent_val):
            if not node:
                return

            if node.val == x:
                self.x = [depth, parent_val]
            elif node.val == y:
                self.y = [depth, parent_val]
                
            if self.x and self.y:
                return
                
            dfs(node.left, depth + 1, node.val)
            dfs(node.right, depth + 1, node.val)
            
        dfs(root, 0, None)
        x_depth, x_parent = self.x
        y_depth, y_parent = self.y
        return (x_depth == y_depth) and (x_parent != y_parent)