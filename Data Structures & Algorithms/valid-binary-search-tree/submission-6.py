# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    mini={}
    maxi={}
    def minof(self,node):
        if(not node):
            self.mini[node]=1001
            return 1001
        self.mini[node] = min(node.val,min(self.minof(node.left),self.minof(node.right)))
        return self.mini[node]
    def maxof(self,node):
        if(not node):
            self.maxi[node]=-1001
            return -1001
        self.maxi[node] = max(node.val,max(self.maxof(node.left),self.maxof(node.right)))
        return self.maxi[node]
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        a=self.minof(root)
        a=self.maxof(root)
        leftvalid=True
        rightvalid=True
        if not root.left and not root.right:
            return True
        if root.left:
            leftvalid=self.isValidBST(root.left)

        if root.right:
            rightvalid=self.isValidBST(root.right) 

        return self.mini[root.right]>root.val and self.maxi[root.left]<root.val and leftvalid and rightvalid
