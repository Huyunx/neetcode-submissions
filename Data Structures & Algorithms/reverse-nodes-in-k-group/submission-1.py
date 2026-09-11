# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def headofreversed(head):
            n=head
            if(not n):
                return n
            for _ in range(k-1):
                n=n.next
                if(not n):
                    return head
            currnode=head
            prev=None
            for _ in range(k):
                orignext=currnode.next
                currnode.next=prev
                prev=currnode
                currnode=orignext
            newhead=prev
            head.next=headofreversed(currnode)
            return newhead
        return headofreversed(head)