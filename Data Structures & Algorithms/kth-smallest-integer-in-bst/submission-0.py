# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=None
        n=0
        def dfs(root):
            nonlocal n,ans
            if(not root):
                return
            dfs(root.left)
            n+=1
            if(n==k):
                ans=root
                return
            dfs(root.right)
            return
        dfs(root)
        return ans.val