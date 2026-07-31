# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        h=deque()
        h.append(root)
        if(not root):
            return []
        ans=[]
        while h:
            s=len(h)
            ans.append(h[0].val)
            for i in range(s):
                node=h.popleft()
                if(node.right):
                    h.append(node.right)
                if(node.left):
                    h.append(node.left)
        return ans