# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rev(self,a):
        if not a:
            return None
        if not a.next:
            return a
        b=self.rev(a.next)
        a.next.next=a
        a.next=None
        return b
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        b=self.rev(head.next)
        self.reorderList(b)
        head.next=b