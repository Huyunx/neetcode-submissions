# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited={}
        while head:
            visited[head]=visited.get(head,0)+1
            if(visited[head]==2):
                return True
            head = head.next
        return False