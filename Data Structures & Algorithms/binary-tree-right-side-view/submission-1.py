# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        answer = []
        line = deque([root])
        while line:
            size = len(line)

            for i in range(size):
                node = line.popleft()
                if i == size - 1:
                    answer.append(node.val)
                
                if node.left:
                    line.append(node.left)
                if node.right:
                    line.append(node.right)

        return answer