# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodeHelper(self,root,maxval):
        if not root:
            return
        
        if root.val >= maxval:
            self.res += 1
        
        self.goodNodeHelper(root.left,max(maxval,root.val))
        self.goodNodeHelper(root.right,max(maxval,root.val))
        
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        
        self.goodNodeHelper(root,float("-inf"))
        
        return self.res
        
        
        
        
        