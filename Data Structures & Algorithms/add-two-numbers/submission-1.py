# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(n1,n2,jinwei):
            if(not n1  and not n2):
                if(jinwei):
                    return ListNode(jinwei)
                else:
                    return None
            n1next=None
            n2next=None
            n1val=0
            n2val=0
            if(n1):
                n1next=n1.next
                n1val=n1.val
            if(n2):
                n2next=n2.next
                n2val=n2.val
            ret=ListNode((n1val+n2val+jinwei)%10)
            jinwei=(n1val+n2val+jinwei)//10
            nnext=add(n1next,n2next,jinwei)
            ret.next=nnext
            return ret
        return add(l1,l2,0)