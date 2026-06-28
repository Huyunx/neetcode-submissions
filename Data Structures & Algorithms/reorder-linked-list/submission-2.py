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
        #fast and slow pointer 2/1
        fast =head
        slow = head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        mid=slow
        b=self.rev(mid.next)
        mid.next=None
        ans=head
        a=head
        while a and b:
            anext=a.next
            if b:
                bnext=b.next
            a.next=b
            if anext:
                b.next=anext
            a=anext
            if b:
                b=bnext

        

       

