# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSumHelper(self,root)->int:
        if not root:
            return 0
        left = self.maxPathSumHelper(root.left)
        right = self.maxPathSumHelper(root.right)
        
        maxPathSumAtLevel = max(left+root.val,right+root.val,root.val)
        self.maxSum = max(self.maxSum,maxPathSumAtLevel,left+right+root.val)
        
        return maxPathSumAtLevel
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        self.maxPathSumHelper(root)
        return self.maxSum
        
        