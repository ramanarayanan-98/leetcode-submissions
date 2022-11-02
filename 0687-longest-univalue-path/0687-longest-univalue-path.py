# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUVPHelper(self, root):
        if not root.left and not root.right:
            return 0
        
        leftval,rightval = 0,0
        isLeftEqual,isRightEqual = False,False
        if root.left:
            leftval = self.longestUVPHelper(root.left)
            # print(leftval)
            isLeftEqual = root.left.val == root.val
            leftval += 1 if isLeftEqual else 0
        if root.right:
            rightval = self.longestUVPHelper(root.right)
            # print(rightval)
            isRightEqual = root.right.val == root.val
            rightval += 1 if isRightEqual else 0
        
        combined = leftval+rightval if isLeftEqual and isRightEqual else 0
        self.longestLen = max(self.longestLen,leftval,rightval,combined)
        # print(self.longestLen,leftval,rightval,combined)
        # print(id(self.longestLen),id(leftval),id(rightval),id(combined))
        return max(leftval if isLeftEqual else 0,rightval if isRightEqual else 0)
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longestLen = 0
        if not root:
            return self.longestLen
        self.longestUVPHelper(root)
        return self.longestLen