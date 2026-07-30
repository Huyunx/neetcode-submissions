# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def deepness(node):
            nonlocal ans
            l=0
            r=0
            if(node.left):
                l=deepness(node.left)
            if(node.right):
                r=deepness(node.right)
            ans=max(l+r+1,ans)
            return max(l,r)+1
        deepness(root)
        return ans-1
            
            