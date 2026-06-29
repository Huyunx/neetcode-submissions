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
            leng=len(q)  #takes O(n) to copy so that's why its not efficient see sol2,there are ways to avoid copying 
            #essentially we want a condition for the upcomming while loop, which can just use the length of the original queue to tell the repeating times of the following while looop
            l=[]
            for i in range(leng):
                a=q.popleft()
                l.append(a.val)
                if(a.left):
                    q.append(a.left)
                if(a.right):
                    q.append(a.right)
            ans.append(l)

        return ans
    