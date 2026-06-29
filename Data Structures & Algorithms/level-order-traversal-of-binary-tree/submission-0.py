# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        if(root):    
            q.append(root)
        ans=[]
        while q:
            q2=deque(q)
            l=[]
            while q:
                a=q.popleft()
                l.append(a.val)
            ans.append(l)
            while q2:
                a=q2.popleft()
                if(a.left):
                    q.append(a.left)
                if(a.right):
                    q.append(a.right)

        return ans
    