# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq 
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #array of k nodes pointing towarrds the front node
        pq=[]#each element is a pair keeping the value of each
        # front, with which we sort the pq, and also the index of the list that has the lowest front 
        # lists[the index of the list with min front value],i.e. lists[pq.front.second]
        for i,l in enumerate(lists):#what if list[k] is empty, then dont put it in the heap
            if(l):
                heapq.heappush(pq,(l.val,i))
        dummy=ListNode()
        a=dummy
        while pq: #
            index_of_list_with_lowest_front=pq[0][1]
            dummy.next=lists[index_of_list_with_lowest_front]
            dummy=dummy.next
            heapq.heappop(pq)
            addnode=lists[index_of_list_with_lowest_front].next
            lists[index_of_list_with_lowest_front]=lists[index_of_list_with_lowest_front].next#this advancing of list[i] was missing
            if(addnode):
                heapq.heappush(pq,(addnode.val,index_of_list_with_lowest_front))
               
        return a.next