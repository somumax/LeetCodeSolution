# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.findRight(root, 0, res)
        return res
    def findRight(self, root, level, res):
        if root is None:
            return 
        if level == len(res):
            res.append(root.val)
            
        self.findRight(root.right,level+1 , res)
        self.findRight(root.left,level+1 , res)