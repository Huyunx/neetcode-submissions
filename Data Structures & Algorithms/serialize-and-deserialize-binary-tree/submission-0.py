# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if(not root):
                return 'N'
            return str(root.val)+','+dfs(root.left)+','+dfs(root.right)
        return dfs(root)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i=0
        def ans():
            nonlocal i
            s=''
            
            while i<len(data) and data[i]!=',':
                s=s+data[i]
                i+=1
            
            if(s=='N'):
                i+=1
                return None
            value=int(s) 
            a=TreeNode(value)
            i+=1
            a.left=ans()
            a.right=ans()

            return a
        return ans()
