# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a=head
        c=0
        while a:
            c+=1
            a=a.next
        a=head
        dummy=ListNode()
        dummy.next=a
        a=dummy
        for i in range(c-n):
            a=a.next
        if a.next.next:
            a.next=a.next.next
        else:
            a.next=None
        return dummy.next