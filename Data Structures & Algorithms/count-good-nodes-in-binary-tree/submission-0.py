# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxSoFar):

            if node is None:
                return 0

            if node.val >= maxSoFar:
                good = 1
            else:
                good = 0
            
            newMax = max(node.val, maxSoFar)

            left = dfs(node.left, newMax)
            right = dfs(node.right, newMax)
            return good + left + right

        return dfs(root, root.val)