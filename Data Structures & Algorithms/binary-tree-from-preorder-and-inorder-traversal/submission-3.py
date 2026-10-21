class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        position = {value: i for i, value in enumerate(inorder)}
        self.pre = 0

        def build(left, right):
            if left > right:
                return None

            root = TreeNode(preorder[self.pre])
            self.pre += 1

            mid = position[root.val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)