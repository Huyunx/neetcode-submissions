"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        n=head
     
        origtonew={}
        def copyof(head):
            if(not head):
                return None
            if(head in origtonew):
                return origtonew[head]
            ans=Node(head.val)
            origtonew[head]=ans
            ans.next=copyof(head.next)
            
            ans.random=copyof(head.random)
            
            return ans

        return copyof(head)