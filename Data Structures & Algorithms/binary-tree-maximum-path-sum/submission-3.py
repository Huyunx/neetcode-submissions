# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxlinecontain={}
    def maxcontinuoslinecontain(self,root):
        if(not root):
            return -1001
        self.maxlinecontain[root]=max(max(self.maxcontinuoslinecontain(root.left),self.maxcontinuoslinecontain(root.right)),0)+root.val
        return self.maxlinecontain[root]
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxcontinuoslinecontain(root)
        def maxps(root):
            maxlineleft=0
            maxlineright=0
            if(not root):
                return -1001
            if((not root.left) and not root.right):
                return root.val
            if root.left:
                maxlineleft=max(0,self.maxlinecontain[root.left])
            if root.right:
                maxlineright=max(0,self.maxlinecontain[root.right])
            maxsumwithcurrnode=maxlineleft+maxlineright+root.val
            return max(max(maxps(root.left),maxps(root.right)), maxsumwithcurrnode)
        return maxps(root)