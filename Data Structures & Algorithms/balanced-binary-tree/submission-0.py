# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=True
        if(not root):
            return ans
        def deepness(node):
            nonlocal ans
            l=0
            r=0
            if(node.left):
                l=deepness(node.left)
            if(node.right):
                r=deepness(node.right)
            if(abs(l-r)>1):
                ans=False
            return 1+max(l,r)
        deepness(root)
        return ans
            
        