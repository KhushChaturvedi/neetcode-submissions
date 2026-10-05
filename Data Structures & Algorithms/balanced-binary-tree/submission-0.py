# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def depth(node):
            if node is None:
                return 0
            leftDepth = depth(node.left)
            rightDepth = depth(node.right)
            if abs(leftDepth - rightDepth) > 1:
                self.balanced =  False
            return 1 + max(leftDepth, rightDepth)

        depth(root)
        return self.balanced