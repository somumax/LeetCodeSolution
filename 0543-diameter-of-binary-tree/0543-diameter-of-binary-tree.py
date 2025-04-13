# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0  # Initialize diameter

        def findDepthdfs(node):
            nonlocal diameter
            if node is None:
                return 0
            left = findDepthdfs(node.left)
            right = findDepthdfs(node.right)

            # Update diameter at this node
            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        findDepthdfs(root)
        return diameter

