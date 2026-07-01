# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        h={}
        for i,p in enumerate(inorder):
            h[p]=i
        def Tree(prel,prer,inl,inr):
            if prel > prer or inl > inr:#everything was correct the only thing was this edge case
                return None
            a=TreeNode()
            rootval=preorder[prel]
            a.val=rootval
            rootindex_in_inorder=h[rootval]
            
            
            if(prel==prer):
                return a
            if(inl==inr):
                return a
            leftSize=rootindex_in_inorder-inl
            
            a.left=Tree(prel+1,prel+leftSize,inl,rootindex_in_inorder-1)
            a.right=Tree(prel+leftSize+1,prer,rootindex_in_inorder+1,inr)
            return a
        return Tree(0,len(preorder)-1,0,len(inorder)-1)