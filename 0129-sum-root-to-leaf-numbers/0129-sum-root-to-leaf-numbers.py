# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def findsum(root,curSum):
            if not root:
                return 0
            curSum = curSum*10+root.val
            if not root.left and not root.right:
                return curSum
            return findsum(root.left,curSum)+findsum(root.right,curSum)
        val = 0
        res  = findsum(root,val)
        return res
        