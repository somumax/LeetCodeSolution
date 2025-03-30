# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        #Process right subtree first
        self.flatten(root.right)
        #process left subtree
        self.flatten(root.left)
        #set the current node's right
        # to prev and left to None
        root.right = self.prev
        root.left = None
        #update prev to curr node
        self.prev = root

        