# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0
        
        def depth(node):
            if node is None:
                return 0
            
            leftDepth = depth(node.left)
            rightDepth = depth(node.right)
            self.diameter = max(self.diameter, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
        
        depth(root)
        return self.diameter