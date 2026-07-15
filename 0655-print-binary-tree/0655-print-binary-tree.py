# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[str]]
        """
        def height(root):
            if root is None:
                return 0
            lft=height(root.left)
            rgt=height(root.right)
            return 1+max(lft,rgt)
        depth = height(root)
        
        height = depth - 1 
        rows = height + 1
        cols = (2 ** (height + 1)) - 1
        
        res = [[""] * cols for _ in range(rows)]
        
        def populate(node, r, c):
            if not node:
                return
                
            res[r][c] = str(node.val)
            
            if node.left:
                next_c = c - (2 ** (height - r - 1))
                populate(node.left, r + 1, next_c)
                
            if node.right:
                next_c = c + (2 ** (height - r - 1))
                populate(node.right, r + 1, next_c)
                
        populate(root, 0, (cols - 1) // 2)
        
        return res