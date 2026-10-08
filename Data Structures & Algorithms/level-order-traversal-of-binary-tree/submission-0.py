# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
            
        answer = []
        line = deque([root])

        while line:
            level = []
            size = len(line)
            for _ in range(size):
                node = line.popleft()
                level.append(node.val)

                if node.left:
                    line.append(node.left)
                if node.right:
                    line.append(node.right)

            answer.append(level)

        return answer