# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p=head
        arr=[]
        while p:
            arr.append(p)
            p=p.next
        r=len(arr)-1
        l=0
        while r>l:
            arr[l].next=arr[r]
            l+=1
            if(r!=l):
                arr[r].next=arr[l]
            else:
                break
            r-=1
        arr[l].next=None